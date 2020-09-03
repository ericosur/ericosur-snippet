submodules
==========

For first usage:
```
git clone --recursive <repo url>
```

For later usage:
```
git submodule update --init
```

submodule path:

- C/fmt (7.0.3-127-g6cccdc24)
- prime/powmod_test/fast-modular-exponentiation

```
git submodule update --recursive --remote
```

## howto

* add submodule path
```
git submodule add <repo url> <folder>
git commit
git push
```

* remove submodule path

```
git submodule deinit -f <submodule folder>
rm -rf .git/modules/path/to/submodule
git rm -f path/to/submodule
git commit
git push
```

