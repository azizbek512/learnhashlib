#  Kiritilgan ["qwerty", "12345", "admin"] matnlarini hash qilib, yangi faylga yozing.
import hashlib
given_list = ["qwerty", "12345", "admon"]
with open("list_hash.txt", "w") as file:
    hash_list = {hashlib.sha256(item.encode()).hexdigest() for item in given_list}
    file.write(f"given list: {given_list}\n hashed list: {hash_list}")
print("hash result was saved in 'list_hash.txt'")
