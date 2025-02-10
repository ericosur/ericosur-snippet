# README

Here is a simple .net C# cli app that helps to decrypt / encrypt an save file.

## Forword

The save game file is a AES-CBC encrypted json file in base64 format.
There are some strange padding bytes at the end of json file.
At the first time I used python script to do base64 decode and
AES-CBC decryption. It keeps raising excepton about some invalid
byte sequence after decryption / base64.

So I give up the python decryption implementation. I use dotnet
C# implementation that is same as Unity (game engine).

Due to there are some strange bytes at the tail of json file, I
will not use json parse to load and/or modify.

Keep as it. Just maunally modify values as the least fields as possible.
After applying the modified save file, the altered value can be confirmed
as working.

## DecryptApp

This game uses a little old dotnet version. There are some warnings.

```
.../DecryptApp/Crypt.cs(13,42): warning SYSLIB0022: 'RijndaelManaged' is obsolete: 'The Rijndael and RijndaelManaged types are obsolete. Use Aes instead.' (https://aka.ms/dotnet-warnings/SYSLIB0022) [/home/user/src/ericosur-snippet/game/eliminator_kaede/DecryptApp/DecryptApp.csproj]
.../DecryptApp/Crypt.cs(34,42): warning SYSLIB0022: 'RijndaelManaged' is obsolete: 'The Rijndael and RijndaelManaged types are obsolete. Use Aes instead.' (https://aka.ms/dotnet-warnings/SYSLIB0022) [/home/user/src/ericosur-snippet/game/eliminator_kaede/DecryptApp/DecryptApp.csproj]
```

The Rijndael class could be removed in the further version of dotnet. (I cannot promise it will work later.)
