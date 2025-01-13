# Foydalanuvchidan tasodifiy uzunlikdagi matn qabul qilib, hash natijasini qaytaring.
import hashlib
text = input("enter text: ")
hashed = hashlib.sha256(text.encode()).hexdigest()
print("text: ", text)
print("hash: ", hashed)