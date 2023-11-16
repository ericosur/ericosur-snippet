# readme for folder ImageMagick

Most perl scripts here are using Image::Magick to perform image editing.
Some scripts started **gm** are using Graphics::Magick. It is nearly seamless to convert Image::Magick script to Graphics::Magick. Only replace __"Image::Magick"__ to __"Graphics::Magick""__ and get jobs done.

## requirements

```
apt-get install libimage-magick-perl
```

## tips

* extract jpg from nef (nikon raw format)

```exiftool -b -JpgFromRaw sample.nef > sample.jpg```

* make gif from files

```magick convert -delay 150 arr??.gif anim.gif```
