def rc4(key, text):
    S = list(range(256))
    j = 0
    out = []

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        out.append(chr(ord(char) ^ k))

    return ''.join(out)

key = "securekey"
msg = "HELLO"
cipher = rc4(key, msg)
print(cipher)
print(rc4(key, cipher))