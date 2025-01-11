#  Matn uzunligi 10 KB bo‘lgan tasodifiy matn yaratib, uning hashini hisoblang.
import os
import hashlib
random_text = os.urandom(10*1024).hex()
# compute the sha256 hash of the random text
random_hash = hashlib.sha256(random_text.encode()).hexdigest()
print("random text (10KB): ", random_text)
print("hashed text: ", random_hash)