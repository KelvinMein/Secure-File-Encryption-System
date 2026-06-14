ciphertext = "M@IIJ"
key = 5

plaintext = ""

for ch in ciphertext:
    plaintext += chr(ord(ch) ^ key)

print("Ciphertext:", ciphertext)
print("Recovered Plaintext:", plaintext)