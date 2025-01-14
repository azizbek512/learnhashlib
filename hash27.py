# 10 ta tasodifiy matn hashlarini bir faylda saqlang.
import hashlib
import random
import string

def randomtext(length=10):
        text = string.ascii_letters + string.digits
        return ''.join(random.choices(text, k = length))

with open("randomtexthash.txt", "w") as file:
    texts = [randomtext(10) for _ in range(10)]
    hashtext = [hashlib.sha256(texts.encode()).hexdigest for text in texts]
    for text, hash_value in zip(texts, hashtext):
        file.write(f"texts: {text} \n  hashes of them: {hashtext}")
print("enter randomtexthash.txt")