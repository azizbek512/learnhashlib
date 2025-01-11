# Berilgan 10 ta tasodifiy matnning hashlarini hisoblang>>
import hashlib
import random
import string

# tasodifiy matn yaratish funkiyasi>>
def generate_random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# 10 ta tasodifiy matn yaratish>>
random_texts = [generate_random_string() for _ in range(10)]

# har bir matnning sh-256 hashini hisoblash>>
hashes = {}
for text in random_texts:
    hash_object = hashlib.sha256(text.encode()) #matnni kodlab sha-256 hisoblash
    hash_hex = hash_object.hexdigest() #hashni hex formatida olish
    hashes[text] = hash_hex #matn va uning juftligi

# natija
for text, hash_hex in hashes.items():
    print(f"text: {text} -> hash: {hash_hex}")
