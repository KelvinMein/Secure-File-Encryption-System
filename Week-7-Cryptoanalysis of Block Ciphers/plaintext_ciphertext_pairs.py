plaintext = "HELLO"
key = 5

ciphertext = ""

for ch in plaintext:
    ciphertext += chr(ord(ch) ^ key)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)