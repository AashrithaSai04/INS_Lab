def create_matrix(key):
    key=key.upper().replace('J','I')
    key="".join(dict.fromkeys(key))
    alpha="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key+="".join(c for c in alpha if c not in key)
    matrix=[key[i:i+5] for i in range(0,25,5)]
    return matrix

def find_position(matrix,ch):
    for r in range(5):
        for c in range(5):
            if matrix[r][c]==ch:
                return r,c
            
def prepare_text(text):
    text=text.upper().replace('J','I')
    text=''.join(c for c in text if c.isalpha())
    result=""
    i=0

    while i<len(text):
        a=text[i]

        if i+1<len(text):
            b=text[i+1]

            if a==b:
                result+=a+'X'
                i+=1
            else:
                result+=a+b
                i+=2
        else:
            result+=a+'X'
            i+=1
    return result

def encrypt(text,matrix):
    result=""

    for i in range(0,len(text),2):
        a=text[i]
        b=text[i+1]

        r1,c1=find_position(matrix,a)
        r2,c2=find_position(matrix,b)

        if r1==r2:
            result+=matrix[r1][(c1+1)%5]
            result+=matrix[r2][(c2+1)%5]
        elif c1==c2:
            result+=matrix[(r1+1)%5][c1]
            result+=matrix[(r2+1)%5][c2]
        else:
            result+=matrix[r1][c2]
            result+=matrix[r2][c1]
    return result

def decrypt(text,matrix):
    result=""

    for i in range(0,len(text),2):
        a=text[i]
        b=text[i+1]

        r1,c1=find_position(matrix,a)
        r2,c2=find_position(matrix,b)

        if r1==r2:
            result+=matrix[r1][(c1-1)%5]
            result+=matrix[r2][(c2-1)%5]
        elif c1==c2:
            result+=matrix[(r1-1)%5][c1]
            result+=matrix[(r2-1)%5][c2]
        else:
            result+=matrix[r1][c2]
            result+=matrix[r2][c1]
    return result

text=input("Enter plain text: ")
key=input("Enter key: ")

matrix=create_matrix(key)
print("\n Playfair Matrix:")
for row in matrix:
    print(" ".join(row))

prepared_text=prepare_text(text)
enc=encrypt(prepared_text,matrix)
dec=decrypt(enc,matrix)
print("Encrypted text: ",enc)
print("Decrypted text: ",dec)