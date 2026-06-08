from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

message = input("Enter message to encrypt: ").encode()

encrypted = cipher.encrypt(message)

print("Encrypted message:", encrypted.decode())