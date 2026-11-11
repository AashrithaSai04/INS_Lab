import hashlib
msg=input("Enter Message: ")
hash=hashlib.sha256(msg.encode("utf-8")).hexdigest()
print("Sha-256 Hash:",hash)
print("Hash Length:",len(hash), "hex characters")