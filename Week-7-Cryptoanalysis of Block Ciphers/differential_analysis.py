p1 = 10
p2 = 11

c1 = p1 ^ 5
c2 = p2 ^ 5

difference_plain = p1 ^ p2
difference_cipher = c1 ^ c2

print("Plaintext Difference :", difference_plain)
print("Ciphertext Difference:", difference_cipher)