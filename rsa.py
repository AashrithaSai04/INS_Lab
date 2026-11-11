def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def modInverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return -1


def generateKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)
    return e, d, n


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(c, d, n):
    return pow(c, d, n)


p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

e, d, n = generateKeys(p, q)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

M = int(input("Enter message: "))

if M >= n:
    print("Message must be smaller than n.")
    exit()

print("Original Message:", M)

C = encrypt(M, e, n)
print("Encrypted Message:", C)

print("Decrypted Message:", decrypt(C, d, n))