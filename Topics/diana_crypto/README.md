# Diana Cryptosystem

This article describes about [programming praxis][1] or [dodona][2], and how to use.


[1]: https://programmingpraxis.com/2014/12/19/diana-cryptosystem/
[2]: https://dodona.ugent.be/en/exercises/2088793301/

## usage

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

and plain text:
`HELLO WORLD`

then we got:
`BNUVO JOJMR SKWSE IWYZR`
