import hashlib

text = input("Text: ")

hash = hashlib.sha256(text.encode()).hexdigest()
print("Hash:", hash)
