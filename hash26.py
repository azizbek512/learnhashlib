# VI. Hash natijasini saqlash:
# "python2025" matnining hashini faylda saqlang.

import hashlib
text = "python2025"
with open("python2025.txt", "w") as file:
    hash_text = hashlib.sha256(text.encode()).hexdigest()
    file.write(f"text: {text} \n hashed text: {hash_text}")
print("saved in 'python2025.txt' file")
