# katta matnlar bilan ishlash:
# "A" harfini 100 ming marta takrorlash orqali katta matn yarating va uning hashini hisoblang.>>
import hashlib
large_text = "A" * 100000
hash_object = hashlib.sha256(large_text.encode()).hexdigest()
print("result: ", hash_object)