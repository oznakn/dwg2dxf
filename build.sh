#!/bin/bash

rm -rf libdxfrw/

mkdir -p libdxfrw && cd libdxfrw
git init
git remote add origin https://github.com/codelibs/libdxfrw
git fetch origin --depth=1 c84ce8ec12e6523c51c065fc533dfbd095dde953
git reset --hard FETCH_HEAD
rm -rf .git/

mkdir -p build
mkdir -p dwg2dxf/build
echo -e '\n\ninclude_directories(/usr/local/Cellar/libiconv/1.17/include)\nlink_libraries(/usr/local/Cellar/libiconv/1.17/lib PRIVATE)' >> CMakeLists.txt

cp ../dwg2dxfCMakeLists.txt dwg2dxf/CMakeLists.txt

cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --verbose --config Release
cp libdxfrw.a ../dwg2dxf/

cd ../dwg2dxf/build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --verbose --config Release

cp dwg2dxf ../../../
