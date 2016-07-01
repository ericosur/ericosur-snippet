Diana Cryptosystem
==================

This article describes about [Diana Cryptosystem](http://programmingpraxis.com/2014/12/19/diana-cryptosystem/), and how to use.

usage
-----

**how to generate trigraph table**
```
perl print_trigraph.pl > trigraph.txt
```
Here is a pre-generated version: diana_trigraph.docx

**generate OTP**
```
python gen_otp.py > otp.txt
```
**encrypt message**
```
perl enc_diana.pl -f otp.txt -i "Hello world"
```
**decrypt message**
```
perl dec_diana.pl -f otp.txt -i "BNUVO JOJMR SKWSE IWYZR"
```

##Sample OTP
```
BNUVO JOJMR ALSWH VPKPF LDVMN
TXHDI TSOTB QNRCJ YXNBN MIJNP
BWKFL XRPAJ OJDRK ACOWI FBNKR
USYZV LSWUP GLSLL AUNCG OXECI
```
