# har bir hash natijasini alohida yozing
import hashlib
text = input("write smth:")
hashing = hashlib.sha256(text.encode()).hexdigest()
print(hashing)