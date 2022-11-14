{
  "targets": [
    {
      "target_name": "dwg2dxf",
      "sources": [
        "src/dwg2dxf.cc",
        "<!@(node -p \"require('fs').readdirSync('./libdxfrw/src').map(f=>'libdxfrw/src/'+f).join(' ')\")",
        "<!@(node -p \"require('fs').readdirSync('./libdxfrw/src/intern').map(f=>'libdxfrw/src/intern/'+f).join(' ')\")",
        "<!@(node -p \"require('fs').readdirSync('./libdxfrw/dwg2dxf').filter(f => f !== 'main.cpp').map(f=>'libdxfrw/dwg2dxf/'+f).join(' ')\")",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "libdxfrw/src",
        "libdxfrw/src/intern",
        "libdxfrw/dwg2dxf",
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
