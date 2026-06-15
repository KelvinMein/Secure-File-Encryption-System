SBOX = {
    0: 6, 1: 4, 2: 12, 3: 5,
    4: 0, 5: 7, 6: 2, 7: 14,
    8: 1, 9: 15, 10: 3, 11: 13,
    12: 8, 13: 10, 14: 9, 15: 11
}

PBOX = [0, 4, 8, 12,
        1, 5, 9, 13,
        2, 6, 10, 14,
        3, 7, 11, 15]

def to_state(x):
    state = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            shift = 4 * (3 - i) + (3 - j)
            state[i][j] = (x >> shift) & 1
    return state

def from_state(state):
    x = 0
    for i in range(4):
        for j in range(4):
            x = (x << 1) | state[i][j]
    return x

def add_round_key(state, key):
    k = to_state(key)
    for i in range(4):
        for j in range(4):
            state[i][j] ^= k[i][j]
    return state

def sub_bytes(state):
    for i in range(4):
        for j in range(4):
            state[i][j] = SBOX[state[i][j]]
    return state

def shift_rows(state):
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]
    return state

def permute(state):
    flat = sum(state, [])
    new = [0] * 16
    for i in range(16):
        new[PBOX[i]] = flat[i]
    return [new[i:i+4] for i in range(0, 16, 4)]

def encrypt(plain, key, rounds):
    state = to_state(plain)

    print("\nInitial State:", state)

    for r in range(rounds):
        state = add_round_key(state, key)
        state = sub_bytes(state)
        state = shift_rows(state)
        state = permute(state)

        print(f"\nAfter Round {r+1}:", state)

    return from_state(state)

plaintext = int(input("Enter plaintext (integer 0-65535): "))
key = int(input("Enter key (integer 0-65535): "))
rounds = int(input("Enter number of rounds: "))

ciphertext = encrypt(plaintext, key, rounds)

print("\n======================")
print("FINAL CIPHERTEXT:", ciphertext)
print("======================")