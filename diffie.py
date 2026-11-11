p=23
g=5
a=4
b=3
A=pow(g,a,p)
B=pow(g,b,p)
alice_key=pow(B,a,p)
bob_key=pow(A,b,p)
print("public prime:",p)
print("public base:",g)
print("Alice private key:", A)
print("Bob provate key",B)
print("Alice shared secret:", alice_key)
print("Bob shared secret:", bob_key)
if alice_key==bob_key:
    print("key exchange successful")
else:
    print("Key exchange failed")
