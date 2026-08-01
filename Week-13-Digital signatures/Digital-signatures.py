from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.exceptions import InvalidSignature

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

with open("private_key.pem", "wb") as file:
    file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

with open("public_key.pem", "wb") as file:
    file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

message = input("Enter document or text message:\n")

with open("document.txt", "w") as file:
    file.write(message)

signature = private_key.sign(
    message.encode(),
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

with open("signature.sig", "wb") as file:
    file.write(signature)

print("\nDocument and signature saved.")

with open("document.txt", "r") as file:
    document = file.read()

with open("signature.sig", "rb") as file:
    signature = file.read()

try:
    public_key.verify(
        signature,
        document.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is valid.")
except InvalidSignature:
    print("Signature verification failed.")

input("\nModify document.txt if you want, then press Enter to verify again...")

with open("document.txt", "r") as file:
    document = file.read()

try:
    public_key.verify(
        signature,
        document.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature is still valid.")
except InvalidSignature:
    print("Document was modified. Signature verification failed.")