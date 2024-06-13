# submodules

- For first usage:

```
git clone --recursive <repo url>
```

- For later usage:

```
git submodule update --init
```

- Fetch changes from submodule repositories:

```
git submodule update --recursive --remote
```

## note

submodule path:

- C/fmt (7.0.3-127-g6cccdc24)
- prime/powmod_test/fast-modular-exponentiation


## howto

* add submodule path
```
git submodule add <repo url> <folder>
git add ...
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

