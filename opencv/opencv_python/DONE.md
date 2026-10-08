# Done

## Test Asset Inventory

- [x] Download former Imgur images: `deer`, `lena`, and `dallehorse` (formerly `smallhorse`). Original file extensions have not been confirmed.

## Asset Preparation

- [x] Package assets as a Release archive: `ericosur/private`, tag `v0.0.1-alpha`, file `image-assets-v0.0.2.zip`.

## Code Infrastructure

- [x] Add the image asset directory to `.gitignore` (`data/`).
- [x] Create [`fetch_assets.sh`](fetch_assets.sh) to download and unpack the Release archive into `./data/`, with auto-unflattening and `--force` support.

## Organization

- [x] Create sub-folder [`dlib/`](dlib/) and move dlib-related scripts ([`faceland.py`](dlib/faceland.py), [`fooface.py`](dlib/fooface.py)) and notes ([`about-dlib.md`](dlib/about-dlib.md)) into it.
