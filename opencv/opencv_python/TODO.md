# TODO List

This document tracks the remaining test image asset needs, replacement plans, and code refactoring tasks for this project (OpenCV Python Snippets). Completed items are recorded in [`DONE.md`](DONE.md).

## TL;DR

* **Problem**: Imgur static direct URLs no longer work reliably (HTTP 429 / bot blocking), and test image files should not bloat this public repository.
* **Solution**: Test images are archived and hosted in a separate private GitHub Release (`ericosur/private`).
* **Quick Setup**: Run `./fetch_assets.sh` (or `./fetch_assets.sh -i <archive.zip>`) to download and unpack test images directly into `./data/`.
* **Current Status**: Asset package `image-assets-v0.0.2.zip` is available; `fetch_assets.sh` script created with auto-unflattening and `--force` support. `setting.json` already uses the relative `./data` path for `global.image_base_dir`, but `readim.py.path` still contains an absolute path. Next steps are to make configured image paths relative and refactor [`imgur.py`](imgur.py) and [`loadimgur.py`](loadimgur.py).

---

## 1. Test Asset Inventory

### A. Former Imgur Remote Images (Need to be served locally or via Release)
- [ ] **`lego.jpg`**: Used by [`loadimgur.py`](loadimgur.py) (default sample image)
- [ ] **`vwcar.jpg`**: Used by [`imgur.py`](imgur.py) (car candidate image)

### B. Local Images Originally Configured in `setting.json` (Originally expected at `~/Pictures/data`)
- [ ] **`flower_and_bee.jpg`**: Used by [`add_border.py`](add_border.py) (border expansion test image)
- [ ] **`47916-wallpaper.jpg`**: Used by [`split.py`](split.py) (RGB channel splitting and mean preprocessing)
- [ ] **`img2668.jpg`**: Used by [`readim.py`](readim.py) (sequential batch loading and line drawing)
- [ ] **`img2980.jpg`**: Used by [`readim.py`](readim.py) (sequential batch loading and line drawing)
- [ ] **`eefb19f7599a5.jpg`**: Used by [`readim.py`](readim.py) (sequential batch loading and line drawing)

### C. Algorithm-Specific Test Images Hardcoded in Individual Scripts
- [ ] **`top.jpg`**, **`bot.jpg`**: Used by [`cvadd.py`](cvadd.py) (vertical and horizontal image stacking)
- [ ] **`img1.jpg`**, **`img2.jpg`**: Used by [`cvutil.py`](cvutil.py) (horizontal image combination and resizing)
- [ ] **`c50.jpg`**: Used by [`persp-transform/go.sh`](persp-transform/go.sh) (4-point perspective transformation example, e.g. card/document/business card)
- [ ] **`headPose.jpg`**: Used by [`headPose.py`](headPose.py) (3D head pose estimation, requires facial features at specific 2D coordinates)
- [ ] **`./data/*.jpg`**: Used by [`dlib/faceland.py`](dlib/faceland.py) (Dlib 68-point facial landmark detection, requires face images and `shape_predictor_68_face_landmarks.dat`)

---

## 2. Asset Preparation & Replacement Plan

- [ ] **Select, photograph, or crop custom photos (~5 to 8 images)**:
  - **General still life / landscape photos**: Can cover most algorithm tests (replacing `flower_and_bee`, `wallpaper`, `img*`, `top/bot`, `img1/2`, etc.).
  - **Perspective transformation photo**: A flat rectangular object placed on a surface (book, card, or business card to replace `c50.jpg`).
  - **Face photo (optional)**: Required only if running `headPose.py` or `dlib/faceland.py` with clear frontal face features.
- [ ] **Dimensions & file size optimization**:
  - Resize dimensions appropriately (1080p or 2K recommended), keeping individual file sizes within 1MB ~ 3MB.

---

## 3. Code Refactoring Tasks

- [ ] **Avoid full/absolute image paths in `setting.json`**:
  - `global.image_base_dir` already uses relative path `"./data"`; change `readim.py.path` from `"/home/user/Pictures/data"` to a relative path such as `"./data"`.
- [ ] **Refactor `imgur.py` and `loadimgur.py`**:
  - Remove runtime dependencies on unstable external Imgur URLs and read from the local cache directory instead; update the legacy `smallhorse` reference to the asset name `dallehorse`.
