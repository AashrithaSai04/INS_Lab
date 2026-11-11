import math

def determinant(matrix):
    n=len(matrix)

    if n==1:
        return matrix[0][0]
    if n==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]

    det=0

    for j in range(n):
        minor=[[matrix[i][k] for k in range(n) if k!=j]for i in range(1,n)]
        det+=matrix[0][j]*(-1)**j*determinant(minor)
    return det

def mod_inverse(a):
    for i in range(1,26):
        if (a*i)%26==1:
            return i

def inverse_matrix(matrix):
    n=len(matrix)
    d=determinant(matrix)%26
    d_inv=mod_inverse(d)

    cofactor=[[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            minor=[[matrix[r][c] for c in range(n) if c!=j] for r in range(n) if r!=i]
            cofactor[i][j]=(-1)**(i+j)*determinant(minor)
    return [[d_inv*cofactor[j][i]%26 for j in range(n)]for i in range(n)]

def process(text,matrix):
    n=len(matrix)
    text=text.upper().replace(" ","")

    res=""
    while len(text)%n:
        text+='X'
    for i in range(0,len(text),n):
        block=text[i:i+n]
        vector=[ord(c)-65 for c in block]

        for row in matrix:
            res+=chr(sum(row[j]*vector[j] for j in range(n))%26+65)
    return res


key=input("Enter key: ").upper()
text=input("Enter text: ")
n=int(math.sqrt(len(key)))
key_matrix=[[ord(key[i*n+j])-65 for j in range(n)]for i in range(n)]

# Make the key matrix invertible
while math.gcd(determinant(key_matrix), 26) != 1:
    key_matrix[-1][-1] = (key_matrix[-1][-1] + 1) % 26

print("Key matrix:")
for row in key_matrix:
    print(row)
    
enc=process(text,key_matrix)
dec=process(enc,inverse_matrix(key_matrix))
print("Encrypted text: ",enc)
print("Decrypted text: ",dec)
