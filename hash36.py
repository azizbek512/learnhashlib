# VIII. Hashlarni taqqoslang
# Foydalanuvchidan ikkita matn kiriting va ularning hash natijalarini solishtiring.
import hashlib
text1 = input("enter 1st text: ") 
text2 = input("enter 2nd text: ")
hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()
if hash1 == hash2:
    print("hashes are same!")
else:
    print("hashes are different!") 
print("hash1: ", hash1)
print("hash2: ", hash2)