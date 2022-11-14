{
  "targets": [
    {
      "target_name": "dwg2dxf",
      "sources": [
        "src/dwg2dxf.cc",
        "<!@(node -p \"require('fs').readdirSync('./libs/dxfrw/src').map(f=>'libs/dxfrw/src/'+f).join(' ')\")",
        "<!@(node -p \"require('fs').readdirSync('./libs/dxfrw/src/intern').map(f=>'libs/dxfrw/src/intern/'+f).join(' ')\")",
        "<!@(node -p \"require('fs').readdirSync('./libs/dxfrw/dwg2dxf').filter(f => f !== 'main.cpp').map(f=>'libs/dxfrw/dwg2dxf/'+f).join(' ')\")",
        "libs/iconv/libiconv/lib/iconv.c",
        "libs/iconv/libiconv/libcharset/lib/localcharset.c",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "libs/dxfrw/src",
        "libs/dxfrw/src/intern",
        "libs/dxfrw/dwg2dxf",
        "libs/iconv/libiconv/lib",
        "libs/iconv/libiconv/include",
        "libs/iconv/include",
      ],
      "dependencies": [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      "cflags!": ["-fno-exceptions"],
      "cflags_cc!": ["-fno-exceptions"],
      "defines": [
        "NAPI_CPP_EXCEPTIONS",
        "NAPI_VERSION=3",
      ],
      "conditions": [
        [
          'OS=="mac"',
          {
            "link_settings": {
              "libraries": [
                "-Wl,-rpath, ."
              ]
            },
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
              "CLANG_ENABLE_OBJC_ARC": "YES",
              "OTHER_CFLAGS": [
                "-ObjC++",
                "-std=c++17",
              ]
            },
          }
        ],
        [
          'OS=="win"',
          {
            "msvs_settings": {
              "VCCLCompilerTool": {
                "AdditionalOptions": ["/std:c++17"]
              }
            },
          }
        ],
      ]
    }
  ]
}
