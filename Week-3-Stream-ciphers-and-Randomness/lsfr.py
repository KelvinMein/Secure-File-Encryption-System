def lfsr(seed, taps, length):
    state = seed
    result = []

    for _ in range(length):
        xor = 0
        for t in taps:
            xor ^= int(state[t])
        result.append(state[-1])
        state = str(xor) + state[:-1]

    return ''.join(result)

seed = "1100101"
taps = [0, 2]
print(lfsr(seed, taps, 20))