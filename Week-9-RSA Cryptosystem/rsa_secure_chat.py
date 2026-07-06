import random
from math import gcd
from datetime import datetime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime():
    while True:
        p = random.randint(100,300)
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

sender = input("Sender: ")
receiver = input("Receiver: ")
message = input("Message: ")

encrypted = [pow(ord(ch), e, n) for ch in message]

print("\nCiphertext:")
print(encrypted)

decrypted = "".join(chr(pow(c, d, n)) for c in encrypted)

print("\nOriginal Message:")
print(decrypted)

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("chat_history.txt", "a") as file:
    file.write(f"{time}\n")
    file.write(f"{sender} -> {receiver}\n")
    file.write(f"Ciphertext: {encrypted}\n")
    file.write(f"Message: {decrypted}\n\n")

print("\nConversation Saved Successfully.")
