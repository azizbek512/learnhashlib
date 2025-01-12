# "testcase" va "TESTCASE" uchun hashlarni solishtiring.
#  "Python!" va "Python " o‘rtasidagi hash farqini toping.
import hashlib
text1 = "testcase"
text2 = "TESTCASE"
hash1 = hashlib.sha256(text1.encode()).hexdigest()
hash2 = hashlib.sha256(text2.encode()).hexdigest()
if hash1 == hash2:
    print("same!")
else:
    print("different!")
print("text1: ", text1)
print("hash1: ", hash1)
print("text2: ", text2)
print("hash2: ", hash2)