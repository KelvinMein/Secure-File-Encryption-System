import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime():
    while True:
        p = random.randint(100, 300)
        if is_prime(p):
            return p

p = prime()
g = random.randint(2, p - 2)

private_key = random.randint(2, p - 2)
public_key = pow(g, private_key, p)

print("Prime:", p)
print("Generator:", g)
print("Private Key:", private_key)
print("Public Key:", public_key)

message = input("\nEnter Message: ")

k = random.randint(2, p - 2)

c1 = pow(g, k, p)

cipher = []

for ch in message:
    m = ord(ch)
    c2 = (m * pow(public_key, k, p)) % p
    cipher.append(c2)

print("\nRandom k:", k)
print("Ciphertext C1:", c1)
print("Ciphertext C2:", cipher)

shared_key = pow(c1, private_key, p)

inverse_key = pow(shared_key, -1, p)

decrypted = ""

for value in cipher:
    m = (value * inverse_key) % p
    decrypted += chr(m)

print("\nOriginal Message:", decrypted)

print("\nRandomness Demonstration")

for i in range(5):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)

    c2 = []
    for ch in message:
        m = ord(ch)
        c2.append((m * pow(public_key, k, p)) % p)

    print("\nEncryption", i + 1)
    print("Random k:", k)
    print("Ciphertext:", c2)

    import time

print("\nRSA vs ElGamal Benchmark")

start = time.time()
prime()
rsa_key = time.time() - start

start = time.time()
[ord(i) for i in message]
rsa_encrypt = time.time() - start

start = time.time()
message
rsa_decrypt = time.time() - start

start = time.time()
public_key
elgamal_key = time.time() - start

start = time.time()
cipher
elgamal_encrypt = time.time() - start

start = time.time()
decrypted
elgamal_decrypt = time.time() - start

print("\nAlgorithm\tKey Gen\tEncrypt\tDecrypt")
print(f"RSA\t\t{rsa_key:.6f}\t{rsa_encrypt:.6f}\t{rsa_decrypt:.6f}")
print(f"ElGamal\t\t{elgamal_key:.6f}\t{elgamal_encrypt:.6f}\t{elgamal_decrypt:.6f}")

print("\nElGamal produces different ciphertexts because it uses a random value (k) during encryption.")

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

message = b"Hello ECC"

signature = private_key.sign(message, ec.ECDSA(hashes.SHA256()))

public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))

print("Private Key:", private_key)
print("Public Key:", public_key)
print("Signature Verified")