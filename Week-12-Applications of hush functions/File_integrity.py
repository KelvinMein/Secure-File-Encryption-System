import hashlib

def sha256_block_hash(message, block_size=64):
    sha = hashlib.sha256()
    data = message.encode('utf-8')

    for i in range(0, len(data), block_size):
        block = data[i:i + block_size]
        sha.update(block)

    return sha.hexdigest()


def save_message_hash(message, hash_value):
    with open("message_hash.txt", "w") as file:
        file.write("Original Message:\n")
        file.write(message + "\n\n")
        file.write("SHA-256 Hash:\n")
        file.write(hash_value)


def verify_message():
    with open("message_hash.txt", "r") as file:
        lines = file.readlines()

    stored_hash = lines[-1].strip()

    new_message = input("\nEnter message to verify:\n")
    new_hash = sha256_block_hash(new_message)

    print("\nNew Hash:", new_hash)
    print("Stored Hash:", stored_hash)

    if new_hash == stored_hash:
        print("\n✔ Message is authentic. No modification detected.")
    else:
        print("\n✘ Message has been modified.")


print("=== Merkle-Damgård SHA-256 Hashing Application ===")

message = input("Enter your message:\n")
hash_value = sha256_block_hash(message)

print("\nSHA-256 Hash:")
print(hash_value)

save_message_hash(message, hash_value)

print("\nMessage and hash saved to message_hash.txt")

choice = input("\nDo you want to verify another message? (yes/no): ")

if choice.lower() == "yes":
    verify_message()

print("\nProgram Finished.")