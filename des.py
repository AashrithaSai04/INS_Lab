from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


def des_encrypt(message, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    return cipher.encrypt(pad(message.encode(), 8))


def des_decrypt(ciphertext, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 8).decode()


key = input("Enter 8-byte key: ")
message = input("Enter message: ")

encrypted = des_encrypt(message, key)

print("Original Message:", message)
print("Secret Key:", key)
print("Encrypted (Hex):", binascii.hexlify(encrypted).decode())

decrypted = des_decrypt(encrypted, key)

print("Decrypted Message:", decrypted)