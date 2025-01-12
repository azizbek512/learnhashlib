# # # "HelloWorld" matnini 1 MB hajmga yetguncha takrorlang va uning hash qiymatini toping.
# # # import hashlib

# # # text = 
# # # Tasodifiy boshlang'ich so'z uchun 1 MB matn yaratish
# # import math

# # # Tasodifiy boshlang'ich so'z (buni xohlagan so'z bilan almashtirish mumkin)
# # initial_word = "exampleword"
# # word_length = len(initial_word)  # So'zning uzunligi (baytlarda)
# # target_size = 1 * 1024 * 1024  # 1 MB = 1024 * 1024 bayt

# # # Takrorlash kerak bo'lgan sonni hisoblash
# # repeat_count = target_size // word_length

# # # Matnni kerakli marta takrorlash
# # large_text = initial_word * repeat_count

# # # Yetmagan bo'lsa, oxirgi qismga qo'shimcha belgilarni to'ldirish
# # remaining_size = target_size - len(large_text)
# # if remaining_size > 0:
# #     large_text += initial_word[:remaining_size]

# # # Matnning yakuniy uzunligini tekshirish
# # len(large_text)
# # print(large_text)
# # Ixtiyoriy boshlang'ich so'zni kiritish
# def generate_text(target_word, target_size_mb=1):
#     word_length = len(target_word)
#     target_size = target_size_mb * 1024 * 1024  # MB dan baytlarga o'tish

#     # Takrorlash kerak bo'lgan sonni hisoblash
#     repeat_count = target_size // word_length

#     # So'zni kerakli marta takrorlash
#     large_text = target_word * repeat_count

#     # Matnni oxirgi 1 MB ga to'liq qilish
#     remaining_size = target_size - len(large_text)
#     if remaining_size > 0:
#         large_text += target_word[:remaining_size]

#     return large_text, len(large_text)

# # Test: Ixtiyoriy "example" so'zi bilan 1 MB matn yaratish
# example_text, text_size = generate_text("example")
# text_size  # Matn uzunligini qaytarish
# print()
import math
import hashlib
text = "helloword"
text_length = len(text)
target_size = 1*1024*1024
# takrorlash sonini hisob
repeat_count = target_size // text_length
# matnni kerakli marta takrorlash
large_text = text * repeat_count
# yetmagan bolsa, oxirgi qismga qoshimcha belgilarni toldirish
remaining_size = target_size - len(large_text)
if remaining_size > 0:
    large_text += text[:remaining_size]
print("hajm: ", len(large_text))

hash_text = hashlib.sha256(large_text.encode()).hexdigest()
# print("text: ", large_text)
print("hash result: ", hash_text)
