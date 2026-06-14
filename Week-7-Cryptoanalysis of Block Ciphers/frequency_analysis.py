from collections import Counter

ciphertext = "M@IIJ"

freq = Counter(ciphertext)

print("Character Frequencies:")
for char, count in freq.items():
    print(char, ":", count)