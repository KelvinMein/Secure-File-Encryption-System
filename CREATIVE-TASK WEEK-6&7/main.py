from collections import Counter

KEY = 5

def encrypt():
    plaintext = input("Enter plaintext: ")

    ciphertext = ""
    for ch in plaintext:
        ciphertext += chr(ord(ch) ^ KEY)

    print("\nPlaintext :", plaintext)
    print("Ciphertext:", ciphertext)


def decrypt():
    ciphertext = input("Enter ciphertext: ")

    plaintext = ""
    for ch in ciphertext:
        plaintext += chr(ord(ch) ^ KEY)

    print("\nRecovered Plaintext:", plaintext)


def avalanche_test():
    text1 = input("Enter first text: ")
    text2 = input("Enter second text (change one character): ")

    c1 = ''.join(chr(ord(ch) ^ KEY) for ch in text1)
    c2 = ''.join(chr(ord(ch) ^ KEY) for ch in text2)

    max_len = max(len(c1), len(c2))
    c1 = c1.ljust(max_len)
    c2 = c2.ljust(max_len)

    differences = 0

    for a, b in zip(c1, c2):
        if a != b:
            differences += 1

    print("\nCiphertext 1:", c1)
    print("Ciphertext 2:", c2)
    print("Differing Characters:", differences)


def frequency_analysis():
    ciphertext = input("Enter ciphertext: ")

    freq = Counter(ciphertext)

    print("\nFrequency Analysis")
    print("------------------")

    for char, count in freq.items():
        print(f"{char}: {count}")


def known_plaintext_attack():
    plain = input("Known plaintext character: ")
    cipher = input("Matching ciphertext character: ")

    key = ord(plain[0]) ^ ord(cipher[0])

    print("\nRecovered Key:", key)


def differential_analysis():
    p1 = int(input("Enter plaintext value 1: "))
    p2 = int(input("Enter plaintext value 2: "))

    c1 = p1 ^ KEY
    c2 = p2 ^ KEY

    print("\nPlaintext Difference :", p1 ^ p2)
    print("Ciphertext Difference:", c1 ^ c2)


while True:
    print("\n===== Cipher Designer & Attack Simulator =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Avalanche Effect Test")
    print("4. Frequency Analysis")
    print("5. Known Plaintext Attack")
    print("6. Differential Analysis")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        encrypt()

    elif choice == "2":
        decrypt()

    elif choice == "3":
        avalanche_test()

    elif choice == "4":
        frequency_analysis()

    elif choice == "5":
        known_plaintext_attack()

    elif choice == "6":
        differential_analysis()

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")