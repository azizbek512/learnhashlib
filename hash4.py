#  "Azizbek2025" matnining SHA-256 hashini yarating
import hashlib
text = "Azizbek2025"
hashing = hashlib.sha256(text.encode()).hexdigest()
print("text: ", text)
print("hash result: ", hashing)