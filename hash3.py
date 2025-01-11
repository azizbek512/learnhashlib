# "password123" matnining SHA-256 hash qiymatini hisoblang.
import hashlib

text = "password123"
hashing = hashlib.sha256(text.encode()).hexdigest()
print("text: ", text)
print("hashing result: ", hashing)