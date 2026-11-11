import hashlib
p=23
q=11
g=2
x=3
y=pow(g,x,p)

def H(msg):
    return int(hashlib.sha256(msg.encode()).hexdigest(),16)

def sign(msg,k):
    z=H(msg)%q
    r=pow(g,k,p)%q
    k_inv=pow(k,-1,q)
    s=(k_inv*(z+x*r))%q
    return r,s

def verify(msg,signature):
    r,s=signature

    if not(0<r<q and 0<s<q):
        return False

    z=H(msg)%q
    w=pow(s,-1,q)
    u1=(z*w)%q
    u2=(r*w)%q

    v=(pow(g,u1,p)*pow(y,u2,p)%p)%q
    return v==r

msg=input("Enter message:")
k=7
s=sign(msg,k)
print("Digital Signature (r,s):",(s))
if verify(msg,s):
    print("Signature is valid.")
else:
    print("Signature is invalid.")
