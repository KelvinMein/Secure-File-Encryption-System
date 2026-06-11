from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.import_key(open("private.pem").read())
cipher = PKCS1_OAEP.new(key)

encrypted = open("encrypted.bin", "rb").read()
decrypted = cipher.decrypt(encrypted)

print(decrypted.decode())