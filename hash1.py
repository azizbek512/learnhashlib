# oddiy sha-256 hashing bo'yicha 50 ta masala:
# matnni hashing qilish
# python matnining sha256 hashini hisoblash>>
import hashlib
text = "python"
hashing = hashlib.sha256(text.encode()).hexdigest()
print("texy: ", text)
print("result: ", hashing)