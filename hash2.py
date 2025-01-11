# "123456" matnini sha256 hash qiymatini toping:
import hashlib 
text = "123456"
hashing = hashlib.sha256(text.encode()).hexdigest()
print("text: ", text)
print("hash result: ", hashing)