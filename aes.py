from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def aes_encrypt(message, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return cipher.encrypt(pad(message.encode(), AES.block_size))

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

key = input("Enter key (16, 24 or 32 bytes): ")

if len(key) not in [16, 24, 32]:
    print("Key must be 16, 24 or 32 bytes.")
    exit()

message = input("Enter message: ")

encrypted = aes_encrypt(message, key)
print("Original Message:", message)
print("Secret Key:", key)
print("Encrypted (Hex):", binascii.hexlify(encrypted).decode())

decrypted = aes_decrypt(encrypted, key)
print("Decrypted Message:", decrypted)