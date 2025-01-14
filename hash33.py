# "sha256" uchun hashni hisoblang va uning uzunligini tasdiqlang.
import hashlib
text = "sha256"
hash = hashlib.sha256(text.encode()).hexdigest()
length = len(hash)
print(f"text: {text}\nhash: {hash}\nlength: {length}")