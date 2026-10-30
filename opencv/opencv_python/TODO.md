# TODO

Outstanding image and path work for the OpenCV examples. Test assets belong in the ignored `data/` directory; fetch the asset archive with `./fetch_assets.sh` or supply a local archive with `./fetch_assets.sh -i <archive.zip>`.

## Missing image assets

- [ ] Resolve missing `dallehorse.jpg` and `lena.jpg` entries in `setting.json` (`global.images`), used by [`add_border.py`](add_border.py): add the files to `data/` or remove the entries.
- [ ] Add `img2668.jpg`, `img2980.jpg`, and `eefb19f7599a5.jpg` for [`readim.py`](readim.py).
- [ ] Add `top.jpg` and `bot.jpg` for [`cvadd.py`](cvadd.py).
- [ ] Add `img1.jpg` and `img2.jpg` for [`cvutil.py`](cvutil.py).
- [ ] Add `c50.jpg` for [`persp-transform/go.sh`](persp-transform/go.sh), with a flat rectangular subject for perspective correction.
- [ ] Add a `headPose.jpg` image for [`headPose.py`](headPose.py) that matches its hard-coded facial landmark coordinates.
