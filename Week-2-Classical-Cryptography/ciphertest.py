def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

tests = [
    ("HELLO", 3),
    ("WORLD", 3),
    ("CYBER", 5)
]

for text, shift in tests:
    encrypted = caesar_encrypt(text, shift)
    print(f"{text} -> {encrypted} (Shift {shift})")