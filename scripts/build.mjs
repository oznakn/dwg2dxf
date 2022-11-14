import util from 'util';
import path from 'path';

import fs from 'fs-extra';
import rimrafCallback from 'rimraf';

const BASE_PATH = process.cwd();

const rimraf = util.promisify(rimrafCallback);

async function cloneLib(origin, commit, name) {
    const targetPath = path.join(BASE_PATH, 'libs', name);

    await fs.mkdir(targetPath, { recursive: true });
    await rimraf(targetPath);
    await fs.mkdir(targetPath, { recursive: true });

    cd(targetPath);
    await $`git init`;
    await $`git remote add origin ${origin}`;
    await $`git fetch origin --depth=1 ${commit}`;
    await $`git reset --hard FETCH_HEAD`;
    cd(BASE_PATH);
}


await cloneLib('https://github.com/pffang/libiconv-for-Windows', '1353455a6c4e15c9db6865fd9c2bf7203b59c0ec', 'iconv');
await cloneLib('https://github.com/codelibs/libdxfrw', 'c84ce8ec12e6523c51c065fc533dfbd095dde953', 'dxfrw');

await $`yarn prebuildify --strip --napi`;
