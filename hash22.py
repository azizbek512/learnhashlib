# Foydalanuvchidan 3 ta matn qabul qilib, ularning hashlarini ro‘yxatda saqlang.
import hashlib
text1 = input("text1: ")
text2 = input("text2: ")
text3 = input("text3: ")
hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()
hash3 = hashlib.sha256(text3.encode()).hexdigest()
print("hash1: ", hash1)
print("hash2: ", hash2)
print("hash3: ", hash3)