
import util from 'util';
import path from 'path';
import fs from 'fs/promises';
import rimrafCallback from 'rimraf';

const BASE_PATH = process.cwd();

const rimraf = util.promisify(rimrafCallback);

await rimraf('libdxfrw');
await fs.mkdir('libdxfrw', { recursive: true });

cd('libdxfrw');
await $`git init`;
await $`git remote add origin https://github.com/codelibs/libdxfrw`;
await $`git fetch origin --depth=1 c84ce8ec12e6523c51c065fc533dfbd095dde953`;
await $`git reset --hard FETCH_HEAD`;
await rimraf('libdxfrw/.git');

await fs.mkdir(path.join(BASE_PATH, 'libdxfrw/build'), { recursive: true });
await fs.mkdir(path.join(BASE_PATH, 'libdxfrw/dwg2dxf/build'), { recursive: true });

const appendData = await fs.readFile(path.join(BASE_PATH, 'assets/baseCMakeLists.txt'), { encoding: 'utf-8' });
await fs.appendFile(path.join(BASE_PATH, 'libdxfrw/CMakeLists.txt'), '\n\n' + appendData,  { encoding: 'utf-8' });
await fs.copyFile(path.join(BASE_PATH, 'assets/dwg2dxfCMakeLists.txt'), path.join(BASE_PATH, 'libdxfrw/dwg2dxf/CMakeLists.txt'));

cd('build');
await $`cmake .. -DCMAKE_BUILD_TYPE=Release`;
await $`cmake --build . --config Release`;
await $`cp libdxfrw.a ../dwg2dxf/`;

cd('../dwg2dxf/build');
await $`cmake .. -DCMAKE_BUILD_TYPE=Release`;
await $`cmake --build . --config Release`;

cd(BASE_PATH);
await $`yarn prebuildify --strip --napi`;
