
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt(data, key):
    data = b'secret data'
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open("encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()

    return ciphertext


def aes_decrypt(key):
    file_in = open("encrypted.bin", "rb")
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    file_in.close()

    # let's assume that the key is somehow available again
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

# Example usage
plaintext = b"hello world"
key = get_random_bytes(16)
ciphertext = aes_encrypt(plaintext, key)
print(ciphertext)  # prints the encrypted ciphertext

decrypted_plaintext = aes_decrypt(key)
print(decrypted_plaintext)  # prints b"hello world"
