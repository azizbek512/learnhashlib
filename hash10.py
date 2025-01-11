#  ["book", "pen", "notebook"] matnlarining hash qiymatlarini bir xil faylda saqlang.
import hashlib
given_list = ["book", "pen", "notebook"]
with open("hashedlistitem.txt", "w") as file:
    hash_list = {hashlib.sha256(item.encode()).hexdigest() for item in given_list}
    file.write(f"given list: {given_list} \n hashed list: {hash_list}")
print("saved in 'hashedlistitem.txt'")