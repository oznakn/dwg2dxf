import util from 'util';
import path from 'path';
import fs from 'fs/promises';
import rimrafCallback from 'rimraf';

const BASE_PATH = process.cwd();

const rimraf = util.promisify(rimrafCallback);

await rimraf(path.join(BASE_PATH, 'libdxfrw'));
await fs.mkdir(path.join(BASE_PATH, 'libdxfrw'), { recursive: true });

cd('libdxfrw');
await $`git init`;
await $`git remote add origin https://github.com/codelibs/libdxfrw`;
await $`git fetch origin --depth=1 c84ce8ec12e6523c51c065fc533dfbd095dde953`;
await $`git reset --hard FETCH_HEAD`;
await rimraf('libdxfrw/.git');

await $`yarn prebuildify --strip --napi`;
