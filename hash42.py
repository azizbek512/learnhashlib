# 5 ta tasodifiy matn hashini ro‘yxatda saqlang.
import hashlib
import os
def randomtext(length=10):
    random_bites = os.urandom(length)
    return ''.join(chr(b) for b in range(length))

hash_list = []

for _ in range(5):
    text = randomtext(10)
    text_hash = hashlib.sha256(text.encode()).hexdigest()
    hash_list.append((text, text_hash))

for i, (text, hash_value) in enumerate(hash_list, 1):
    print(f"{i}-matn: {text}\nhash: {hash_value}\n")
    
print("list: ", hash_list)