# Har birining uzunligi 1 KB bo‘lgan 5 ta matn yarating va hashlarini hisoblang.
import hashlib
import os
# enter 1kb random text
text1 = os.urandom(1*1024).hex()
text2 = os.urandom(1*1024).hex()
text3 = os.urandom(1*1024).hex()
text4 = os.urandom(1*1024).hex()
text5 = os.urandom(1*1024).hex()

# change hash them>>
hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()
hash3 = hashlib.sha256(text3.encode()).hexdigest()
hash4 = hashlib.sha256(text4.encode()).hexdigest()
hash5 = hashlib.sha256(text5.encode()).hexdigest()

# print them
print(f"hash1: { hash1}")
print(f"hash2: { hash2}")
print(f"hash3: { hash3}")
print(f"hash4: { hash4}")
print(f"hash5: { hash5}")
