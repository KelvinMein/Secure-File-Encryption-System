import random
import hashlib
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime():
    while True:
        p = random.randint(100, 300)
        if is_prime(p):
            return p

def inverse(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d

p = prime()
q = prime()

while p == q:
    q = prime()

n = p * q
phi = (p - 1) * (q - 1)

e = 17
while gcd(e, phi) != 1:
    e += 2

d = inverse(e, phi)

print("Prime P:", p)
print("Prime Q:", q)
print("Modulus n:", n)
print("Euler Totient:", phi)
print("Public Key:", (e, n))
print("Private Key:", (d, n))

message = input("\nEnter Message: ")

encrypted = []

print("\nOriginal\tASCII\tEncrypted")

for ch in message:
    ascii_value = ord(ch)
    cipher = pow(ascii_value, e, n)
    encrypted.append(cipher)
    print(f"{ch}\t\t{ascii_value}\t{cipher}")

print("\nDecrypted Message")

decrypted = ""

for value in encrypted:
    ascii_value = pow(value, d, n)
    decrypted += chr(ascii_value)

print("Encrypted:", encrypted)
print("Original Message:", decrypted)

hash_value = hashlib.sha256(message.encode()).hexdigest()

hash_int = int(hash_value, 16) % n

signature = pow(hash_int, d, n)

print("\nOriginal Hash:")
print(hash_value)

print("\nDigital Signature:")
print(signature)

recovered_hash = pow(signature, e, n)

print("\nRecovered Hash:", recovered_hash)

if recovered_hash == hash_int:
    print("Signature Valid")
else:
    print("Signature Invalid")

print("\nMiller-Rabin Prime Test")
print("Number\tResult")

for _ in range(10):
    number = random.randint(2, 200)

    if is_prime(number):
        print(number, "\tProbably Prime")
    else:
        print(number, "\tComposite")