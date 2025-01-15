# Tasodifiy uzunlikdagi 3 ta matn yaratib, hash natijalarini faylga yozing.
import hashlib
text1 = input("text1: ")
text2 = input("text2: ")
text3 = input("text3: ")
with open("random.txt", "w") as file:
    hash1 = hashlib.sha256(text1.encode()).hexdigest()
    hash2 = hashlib.sha256(text2.encode()).hexdigest()
    hash3 = hashlib.sha256(text3.encode()).hexdigest()
    file.write(f"text1: {text1}>>{hash1}\ntext2: {text2}>>{hash2}\ntext3: {text3}>>{hash3}")
print("you can see it in random.txt file")