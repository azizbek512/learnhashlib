# "hello world" va "hello_world" uchun hashlarni hisoblang va taqqoslang
import hashlib
text1 = "hello world"
text2 = "hello_world"
hashing1 = hashlib.sha256(text1.encode()).hexdigest()
hashing2 = hashlib.sha256(text2.encode()).hexdigest()
if hashing1 == hashing2:
    print("same!")
else:
    print("different!")
print("text1: ", text1)
print("1st hashing: ", hashing1)
print("text2: ", text2)
print("2nd hashing: ", hashing2)