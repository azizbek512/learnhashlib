# os kutubxonasi bilan ishlash
import hashlib
import os

def randomtext(length=10):
    random_bytes = os.urandom(length)
    return ''.join(chr(b) for b in random_bytes) # agar ascii yoki unicode ni cheklamoqchi bolsang, % va + operatorini ishlatishing kerak

text = randomtext(10)
hashing = hashlib.sha256(text.encode()).hexdigest()
print(f"text: {text}\nhash: {hashing}")