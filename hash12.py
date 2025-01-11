# "Azizbek" matnini 10 marta qo‘shib yangi matn yarating, so‘ngra uning hashini oling.
import hashlib
text = "Myname" * 10
hashed = hashlib.sha256(text.encode()).hexdigest()
print("text: ", text)
print("hashed text: ", hashed)