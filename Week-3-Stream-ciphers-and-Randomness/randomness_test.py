from collections import Counter

sequence = "11001010101100101010"

count = Counter(sequence)
ones = count['1']
zeros = count['0']

print("Ones:", ones)
print("Zeros:", zeros)

ratio = ones / len(sequence)
print("Ratio of ones:", ratio)