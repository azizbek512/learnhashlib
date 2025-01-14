# TASODIFIY MATNLAR HASHING:
# tasodifiy matnlar yaratib ularni hash qiymatini hisoblang>>
import hashlib
import random
import string
def randomtext(length=10):
    text = string.ascii_letters + string.digits
    return ''.join(random.choices(text, k=length))

text = randomtext(10)
hashing = hashlib.sha256(text.encode()).hexdigest()
print(f"text: {text}\nhash: {hashing}")