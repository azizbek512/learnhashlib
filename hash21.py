# Foydalanuvchidan matn qabul qilib, uning hash qiymatini hisoblang.
import hashlib
text = input("enter text to change hash: ")
hashed = hashlib.sha256(text.encode()).hexdigest()
print("result: ", hashed)