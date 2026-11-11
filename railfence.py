def encrypt(text,key):
    rails=['']*key
    row=0
    dir=1
    for ch in text:
        rails[row]+=ch

        if row==0:
            dir=1
        elif row==key-1:
            dir=-1
        row+=dir
    return "".join(rails)

def decrypt(cipher,key):
    row,dir=0,1
    pattern=[]

    for i in range(len(cipher)):
        pattern.append(row)
        if row==0:
            dir=1
        elif row==key-1:
            dir=-1
        row+=dir

    counts=[pattern.count(i) for i in range(key)]
    rails=[]
    start=0

    for ct in counts:
        rails.append(list(cipher[start:start+ct]))
        start+=ct
    res=''
    for r in pattern:
        res+=rails[r].pop(0)

    return res

text = input("Enter text: ")
key = int(input("Enter number of rails: "))

enc = encrypt(text, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)

