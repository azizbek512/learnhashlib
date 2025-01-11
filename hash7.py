# . ["data", "science", "AI"] matnlarining hashlarini ro‘yxat ko‘rinishida chiqaring
import hashlib

given_list = ["data", "science", "AI"]
hash_list = {hashlib.sha256(list_item.encode()).hexdigest() for list_item in given_list}
print("given list: ", given_list)
print("hashed list: ", hash_list)