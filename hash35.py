# "Matn" va "Matn " hash natijalarini tushuntiring.
import hashlib 
text1 = "Matn"
text2 = "Matn"
hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()
print(f"text1: {text1}; hash1: {hash1}\ntext1: {text2}; hash2: {hash2}")
print('you can see texts and hashes same ')