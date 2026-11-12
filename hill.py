import numpy as np

def encrypt(K, pt):
    pt = pt.upper().replace(" ", "")

    while len(pt) % 3 != 0:
        pt += "X"

    ct = ""

    for i in range(0, len(pt), 3):
        P = np.array([ord(ch)-65 for ch in pt[i:i+3]])
        C = np.dot(K, P) % 26
        ct += ''.join(chr(int(x)+65) for x in C)

    return ct


def decrypt(K, ct):
    det = int(round(np.linalg.det(K))) % 26
    det_inv = pow(det, -1, 26)
    adj = np.array([
        [
            K[1,1]*K[2,2] - K[1,2]*K[2,1],
            K[0,2]*K[2,1] - K[0,1]*K[2,2],
            K[0,1]*K[1,2] - K[0,2]*K[1,1]
        ],
        [
            K[1,2]*K[2,0] - K[1,0]*K[2,2],
            K[0,0]*K[2,2] - K[0,2]*K[2,0],
            K[0,2]*K[1,0] - K[0,0]*K[1,2]
        ],
        [
            K[1,0]*K[2,1] - K[1,1]*K[2,0],
            K[0,1]*K[2,0] - K[0,0]*K[2,1],
            K[0,0]*K[1,1] - K[0,1]*K[1,0]
        ]
    ])
    K_inv = (det_inv * adj) % 26

    pt = ""

    for i in range(0, len(ct), 3):
        C = np.array([ord(ch)-65 for ch in ct[i:i+3]])
        P = np.dot(K_inv, C) % 26
        pt += ''.join(chr(int(x)+65) for x in P)

    return pt

key=input("Enter key: ").upper()
K=np.array([ord(ch)-65 for ch in key]).reshape(3,3)
pt=input("Enter Plain text: ")
print("Key matrix: ")
print(K)

enc=encrypt(K,pt)
print("Encrypted text: ",enc)
print("Decrypted text: ",decrypt(K,enc))