import hashlib

with open("test.txt", "rb") as f:
    data = f.read()

hash = hashlib.sha256(data).hexdigest()
print("Datei Hash:", hash)
