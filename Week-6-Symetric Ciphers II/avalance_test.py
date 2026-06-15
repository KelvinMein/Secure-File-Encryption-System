a = 0b1010101010101010
b = 0b1010101010101011

difference = bin(a ^ b).count("1")

print("Input A:", bin(a))
print("Input B:", bin(b))
print("Differing Bits:", difference)