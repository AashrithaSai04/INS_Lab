import numpy as np

def encrypt(K, pt):
    pt = pt.upper().replace(" ", "")

    while len(pt) % 3 != 0:
        pt += "X"

    ct = ""

    for i in range(0, len(pt), 3):
        P = np.array([ord(ch) - 65 for ch in pt[i:i+3]])
        C = np.dot(K, P) % 26
        ct += "".join(chr(int(x) + 65) for x in C)

    return ct


def decrypt(K, ct):
    det = int(round(np.linalg.det(K)))
    det_inv = pow(det, -1, 26)

    adj = np.round(det * np.linalg.inv(K)).astype(int) % 26
    K_inv = (det_inv * adj) % 26

    pt = ""

    for i in range(0, len(ct), 3):
        C = np.array([ord(ch) - 65 for ch in ct[i:i+3]])
        P = np.dot(K_inv, C) % 26
        pt += "".join(chr(int(x) + 65) for x in P)

    return pt


key = input("Enter Key (9 chars): ").upper()
K = np.array([ord(ch) - 65 for ch in key]).reshape(3, 3)

pt = input("Enter plaintext: ").upper()

print("Key Matrix:")
print(K)

enc = encrypt(K, pt)
print("Ciphertext:", enc)

dec = decrypt(K, enc)
print("Decrypted Text:", dec)