import random

seed = 42
random.seed(seed)

seq = [random.randint(0, 1) for _ in range(20)]
print(seq)