def encrypt(text, key):
    n = len(key)

    while len(text) % n:
        text += 'X'

    rows = len(text) // n
    matrix = [text[i:i+n] for i in range(0, len(text), n)]

    order = sorted(range(n), key=lambda i: key[i])

    return ''.join(matrix[r][c] for c in order for r in range(rows))


def decrypt(cipher, key):
    n = len(key)
    rows = len(cipher) // n

    order = sorted(range(n), key=lambda i: key[i])
    matrix = [[''] * n for _ in range(rows)]

    k = 0

    for c in order:
        for r in range(rows):
            matrix[r][c] = cipher[k]
            k += 1

    return ''.join(''.join(row) for row in matrix)


text = input("Enter text: ").replace(" ", "")
key = input("Enter key: ").upper()

enc = encrypt(text, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)




