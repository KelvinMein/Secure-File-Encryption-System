SBOX = {
    0:14, 1:4, 2:13, 3:1,
    4:2, 5:15, 6:11, 7:8,
    8:3, 9:10, 10:6, 11:12,
    12:5, 13:9, 14:0, 15:7
}

PBOX = [0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15]

def substitute(block):
    result = 0

    for i in range(4):
        nibble = (block >> (i * 4)) & 0xF
        result |= SBOX[nibble] << (i * 4)

    return result

def permute(block):
    result = 0

    for i in range(16):
        bit = (block >> i) & 1
        result |= bit << PBOX[i]

    return result

def encrypt(block, key, rounds):
    for r in range(rounds):
        block ^= key
        block = substitute(block)
        block = permute(block)

        print(f"Round {r+1}: {bin(block)}")

    return block

plaintext = int(input("Enter plaintext (0-65535): "))
key = int(input("Enter key (0-65535): "))
rounds = int(input("Enter number of rounds: "))

ciphertext = encrypt(plaintext, key, rounds)

print("\nCiphertext:", ciphertext)

print("\n--- Avalanche Effect Test ---")

modified_plaintext = plaintext ^ 1

cipher1 = encrypt(plaintext, key, rounds)
cipher2 = encrypt(modified_plaintext, key, rounds)

difference = bin(cipher1 ^ cipher2).count("1")

print("\nOriginal Plaintext :", plaintext)
print("Modified Plaintext :", modified_plaintext)
print("Differing Cipher Bits:", difference)