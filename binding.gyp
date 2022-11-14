{
  "targets": [
    {
      "target_name": "dwg2dxf",
      "sources": [
        "src/dwg2dxf.cc"
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "libdxfrw/src",
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
            "sources": [
                "src/dwg2dxf.cc"
            ],
            "link_settings": {
              "libraries": [
                "-Wl,-rpath, .",
                "-L<(module_root_dir)/libdxfrw/dwg2dxf/build",
                "-ldwg2dxf",
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
            "sources": [
                "src/dwg2dxf.cc"
            ],
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
