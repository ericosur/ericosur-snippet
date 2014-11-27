#
# in ericosur's my own words,
# hash values signed by my own private key => signature
#

# use RSA to sign and verify

http://www.codealias.info/technotes/openssl_rsa_sign_and_verify_howto

# step 1
$ openssl genrsa -out private.pem 1024
$ openssl rsa -in private.pem -out public.pem -outform PEM -pubout

# step 2
$ echo 'data to sign' > data.txt
$ openssl dgst -sha256 < data.txt > hash

# step 3
$ openssl rsautl -sign -inkey private.pem -keyform PEM -in hash > signature

transfer 'data.txt' and 'signature' to recv endpoint
(of course public key is already exchanged)

------------------------------------------------------------

# step 4 (at recv endpoint)
# get hash of data
$ openssl dgst -sha256 < data.txt > myhash

# step 5 (at recv endpoint)
$ openssl rsautl -verify -inkey public.pem -keyform PEM -pubin \
>	-in signature > verified
$ diff -s verified myhash


part 2
https://www.madboa.com/geek/openssl/#digest-sign

# signed digest will be foo.sha1
$ openssl dgst -sha1 \
    -sign private.pem \
    -out foo.sha1 \
    data.txt

# verify data.txt using foo.sha1
$ openssl dgst -sha1 \
    -verify public.pem \
    -signature foo.sha1 \
    data.txt

##############################
http://blog.sina.com.cn/s/blog_a9303fd90101jmtx.html

http://stackoverflow.com/questions/22212869/how-can-i-generate-an-android-keystore-from-a-key-pk8-and-certificate-pem

$ openssl pkcs8 -inform DER -nocrypt -in key.pk8 -out key.pem
$ openssl pkcs12 -export -in certificate.pem -inkey key.pem \
	-out platform.p12 -password pass:android -name mykey
$ keytool -importkeystore -deststorepass password \
	-destkeystore .keystore -srckeystore platform.p12 \
	-srcstoretype PKCS12 -srcstorepass android
$ keytool -list -v -keystore .keystore

http://jmlinnik.blogspot.fi/2011/12/keystores.html

how to make your own x509 certificate
http://www.imacat.idv.tw/tech/sslcerts.html.zh-tw

