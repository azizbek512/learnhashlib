# "Python" matni uchun hash natijasi har doim bir xil bo‘lishini ko‘rsating
import hashlib
text = "python"
text2 = "python"
hashed = hashlib.sha256(text.encode()).hexdigest()
hashed2 = hashlib.sha256(text2.encode()).hexdigest()
print(f"1st text: {text}; hash1: {hashed} \n2nd text: {text2}; hash2: {hashed2}")
print("same, because same😊")