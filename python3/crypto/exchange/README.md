# Exchange - AES Encryption/Decryption Utilities

Utilities for encrypting and decrypting files using AES-256-CBC with PyCryptodome.

## Scripts

### t0.py - Main encryption/decryption tool
Test and demonstrate AES-256-CBC encryption/decryption with key and IV management.

- Encrypts files with AES/CBC/PKCS7Padding
- Supports multiple output formats: binary, base64 (single line), base64 (multi-line)
- Decrypts from various formats
- Manages key/IV from environment variables, binary files, or generates new ones
- Saves key/IV to `key_iv.txt`, `key.bin`, `iv.bin`

**Usage:**
```bash
# Set environment variables
export KEY=<hex-encoded-256-bit-key>
export IV=<hex-encoded-128-bit-iv>

# Run the tool
python3 t0.py
```

### p0.py - Test key generation
Quick test script to verify key generation from environment variables.

**Usage:**
```bash
export KEY=bbc9d7a1e5ddb0f4d62b700c501375517edbc69f674aedd99a64120b240685ce
python3 p0.py
```

### keyiv.py - Key/IV utility module
Provides functions for:
- Loading key/IV from binary files
- Loading key/IV from environment variables (hex-encoded)
- Generating random key/IV
- Saving binary data to files

### exchange_common.py - Common utilities
Provides logging utilities (`prt`, `logd`) using the madlog module.

## Dependencies

- `pycryptodome` - For AES encryption/decryption
- `loguru` - For logging (optional, falls back to print)
- Project modules: `madlog`, `myutil`

**Install:**
```bash
pip install pycryptodome loguru
```

## Environment Variables

- `KEY` - 256-bit AES key in hexadecimal format (64 hex characters)
- `IV` - 128-bit initialization vector in hexadecimal format (32 hex characters)

## OpenSSL Compatibility

The tool is compatible with OpenSSL AES-256-CBC encryption:

```bash
# Encrypt with openssl
export KEY=bbc9d7a1e5ddb0f4d62b700c501375517edbc69f674aedd99a64120b240685ce
export IV=f1606a985ecd3d4e345ea9afc9f2cb98

openssl enc -e -aes-256-cbc -salt -in a.zip -out a.zip.enc -K $KEY -iv $IV

# Decrypt with openssl
openssl enc -d -aes-256-cbc -in a.zip.enc -out a.zip.dec -K $KEY -iv $IV
```

## Output Files

- `a.zip.enc` - Binary encrypted file
- `a.zip.enc.b64` - Base64 encoded, multi-line format
- `a.zip.enc1.b64` - Base64 encoded, single line format
- `key_iv.txt` - Saved key/IV in base64 format
- `key.bin` - Binary key file
- `iv.bin` - Binary IV file
