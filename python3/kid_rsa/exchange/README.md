# README

## openssl

- enc aes-256-cbc salt

```bash
export KEY=bbc9d7a1e5ddb0f4d62b700c501375517edbc69f674aedd99a64120b240685ce
export IV=f1606a985ecd3d4e345ea9afc9f2cb98

openssl enc -e -aes-256-cbc -salt -in a.zip -out a.zip.enc -K $KEY -iv $IV
```
