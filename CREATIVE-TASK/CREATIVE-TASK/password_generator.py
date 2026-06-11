import secrets
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(secrets.choice(chars) for _ in range(length))

print("Generated Password:", password)