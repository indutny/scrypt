{
  "targets": [{
    "target_name": "scrypt",
    "type": "<(library)",
    "include_dirs": [
      ".",
      "include",
    ],
    "direct_dependent_settings": {
      "include_dirs": [
        "include"
      ],
    },
    "sources": [
      "src/backend.c",
      "src/salsa20.c",
      "src/scrypt.c",
      "src/sha256.c",
      "src/pbkdf2.c",
    ],
    "conditions": [
      # Platform-specifics
      ["OS == 'mac'", {
        "sources": [
          "src/backend/osx.c",
        ],
      }],
    ],
  }, {
    "target_name": "test",
    "type": "executable",

    "dependencies": [
      "scrypt",
    ],

    "include_dirs": [
      "."
    ],

    "sources": [
      "test/test.c",

      "test/salsa20.c",
      "test/sha256.c",
      "test/scrypt.c",
      "test/pbkdf2.c",
    ],
  }]
}
