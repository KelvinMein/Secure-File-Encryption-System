plaintext_char = 'H'
ciphertext_char = 'M'

key = ord(plaintext_char) ^ ord(ciphertext_char)

print("Recovered Key:", key)