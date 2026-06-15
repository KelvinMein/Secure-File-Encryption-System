from collections import Counter

def diff(p1, p2):
    return p1 ^ p2

def avalanche(p1, p2):
    return bin(p1 ^ p2).count("1")

def frequency(text):
    return Counter(text)

print("\n=== SECURITY ANALYZER ===")

p1 = int(input("Enter plaintext 1: "))
p2 = int(input("Enter plaintext 2: "))

d = diff(p1, p2)
a = avalanche(p1, p2)

print("\nDifference:", d)
print("Avalanche Effect:", a)

text = input("\nEnter ciphertext text: ")
freq = frequency(text)

print("\nFrequency Distribution:")
for k, v in freq.items():
    print(k, "->", v)

print("\nStatistical Observation:")
if a > 8:
    print("Strong diffusion detected")
else:
    print("Weak diffusion detected")