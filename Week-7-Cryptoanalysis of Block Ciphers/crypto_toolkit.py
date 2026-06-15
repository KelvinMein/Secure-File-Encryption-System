from collections import Counter

def difference(p1, p2):
    return p1 ^ p2

def frequency_analysis(text):
    freq = Counter(text)
    print("\nFrequency Analysis:")
    for k, v in freq.items():
        print(k, ":", v)

def avalanche(p1, p2):
    d = p1 ^ p2
    return bin(d).count("1")

p1 = int(input("Plaintext 1: "))
p2 = int(input("Plaintext 2: "))

print("\nDifference:", difference(p1, p2))
print("Avalanche bits:", avalanche(p1, p2))

txt = input("\nEnter text for frequency analysis: ")
frequency_analysis(txt)