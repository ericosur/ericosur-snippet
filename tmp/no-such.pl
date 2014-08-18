
$req = "require No::Such::Module";
eval $req;
print $@;

$req = "require Image::Magick";
eval $req;
print $@;
