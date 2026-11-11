def encrypt(text,k):
    s=""
    for i in text:
        if 'A'<=i<='Z':
            s+=chr((ord(i)-ord('A')+k)%26+ord('A'))
        elif 'a'<=i<='z':
            s+=chr((ord(i)-ord('a')+k)%26+ord('a'))
        else:
            s+=i
    return s

def decrypt(text,k):
    s=""
    for i in text:
        if 'A'<=i<='Z':
            s+=chr((ord(i)-ord('A')-k)%26+ord('A'))
        elif 'a'<=i<='z':
                s+=chr((ord(i)-ord('a')-k)%26+ord('a'))
        else:
            s+=i
    return s

text=input("Enter plain text: ")
k=int(input("Enter Key: "))
enc=encrypt(text,k)
print("Encrypted text: ",enc)
print("Decrypted text: ",decrypt(enc,k))
