SBOX = {
    '0': 'E',
    '1': '4',
    '2': 'D',
    '3': '1',
    '4': '2',
    '5': 'F',
    '6': 'B',
    '7': '8',
    '8': '3',
    '9': 'A',
    'A': '6',
    'B': 'C',
    'C': '5',
    'D': '9',
    'E': '0',
    'F': '7'
}

PERMUTATION = [0, 4, 8, 12, 1, 5, 9, 13,
               2, 6, 10, 14, 3, 7, 11, 15]

def substitute(text):
    result = ""
    for char in text:
        result += SBOX.get(char.upper(), char)
    return result

def permute(binary):
    output = ['0'] * 16

    for i in range(16):
        output[PERMUTATION[i]] = binary[i]

    return ''.join(output)

plaintext = input("Enter 4-digit hexadecimal plaintext (e.g. 1234): ")

print("\nOriginal Plaintext :", plaintext)

substituted = substitute(plaintext)

print("After Substitution :", substituted)

binary_text = bin(int(substituted, 16))[2:].zfill(16)

print("Binary Form        :", binary_text)

permuted = permute(binary_text)

print("After Permutation  :", permuted)

ciphertext = hex(int(permuted, 2))[2:].upper()

print("Ciphertext         :", ciphertext)