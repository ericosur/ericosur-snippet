
Diana Cryptosystem
------------------

reference:

http://programmingpraxis.com/2014/12/19/diana-cryptosystem/
http://home.earthlink.net/~specforces/spdiana.htm


usage
-----

0. generate trigraph table
$ ./print_trigraph.pl > trigraph.txt

Here is a generated version:
diana_trigraph.docx

1. generate OTP
$ ./gen_otp.py > otp.txt

2. encrypt message
$ ./enc_diana.pl -f otp.txt -i "Hello world"

3. decrypt message
$ ./dec_diana.pl -f otp.txt -i "BNUVO JOJMR SKWSE IWYZR"





OTP
---
BNUVO JOJMR ALSWH VPKPF LDVMN
TXHDI TSOTB QNRCJ YXNBN MIJNP
BWKFL XRPAJ OJDRK ACOWI FBNKR
USYZV LSWUP GLSLL AUNCG OXECI

