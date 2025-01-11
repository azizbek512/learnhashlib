# matnlarni ro'yxatda hashing qilish:
# ["apple", "orange", "banana"] uchun har birining hashini hisoblang.
import hashlib
given_list = ["apple", "orange", "banana"]
item_hashes = {hashlib.sha256(item.encode()).hexdigest() for item in given_list}
print("list result: ", item_hashes)