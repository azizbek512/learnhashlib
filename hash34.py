#  SHA-256 hash natijasining baytlar ko‘rinishini chiqarib bering
import hashlib
text = "SHA-256"
hash_text = hashlib.sha256(text.encode()).digest()
bits = ''.join(f'{bayt:08b}' for bayt in hash_text)

print("text: ", text)
print("sha-256 digest: ", hash_text.hex())
print("bits: ", bits)