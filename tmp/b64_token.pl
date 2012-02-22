use MIME::Base64;

$user = q(rasmus.lai);
$pass = q(adj123);
print encode_base64("\000$user\000$pass");
