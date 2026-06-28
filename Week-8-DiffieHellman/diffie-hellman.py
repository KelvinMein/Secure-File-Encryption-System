p = int(input("Public Prime (p): "))
g = int(input("Generator (g): "))

alice_secret = int(input("Alice Secret Key: "))
bob_secret = int(input("Bob Secret Key: "))

alice_public = pow(g, alice_secret, p)
bob_public = pow(g, bob_secret, p)

alice_shared = pow(bob_public, alice_secret, p)
bob_shared = pow(alice_public, bob_secret, p)

print("\nPublic Prime (p):", p)
print("Generator (g):", g)

print("\nAlice Secret Key:", alice_secret)
print("Bob Secret Key:", bob_secret)

print("\nAlice Public Key:", alice_public)
print("Bob Public Key:", bob_public)

if alice_shared == bob_shared:
    print("\nShared Secret:", alice_shared)
    print("Both users obtained the same secret key.")
else:
    print("\nThe shared secrets do not match.")