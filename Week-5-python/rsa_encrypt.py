from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

message = input("Enter message: ").encode()

key = RSA.import_key(open("public.pem").read())
cipher = PKCS1_OAEP.new(key)

encrypted = cipher.encrypt(message)

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

print("Encrypted (short view):", encrypted[:30])