#  Matnning boshida yoki oxirida bo‘shliq bo‘lsa, hashing jarayonini farqlashni ko‘rsating.
import hashlib
text = input("enter text(if you want, you can write text with space): ")
hash_orginal = hashlib.sha256(text.encode()).hexdigest()

trimmed_text = text.strip() #.strip orqali matn dagi bosh joylar olib tashlanadi
hash_trimmed = hashlib.sha256(trimmed_text.encode()).hexdigest()

print("\n writed text: ")
print(f"{text}")
print(f"hash result (orginal): {hash_orginal}")

print("\n unspaced text: ")
print(f"'{trimmed_text}'")
print(f"hash result (unspaced text): {hash_trimmed}")

if hash_orginal == hash_trimmed:
    print("\n hash results same")
else:
    print("\n hash results different")