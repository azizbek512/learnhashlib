# Matn o‘rniga tasodifiy raqamlar hashingini hisoblang.
import hashlib
import os
def randomnumbers(length=10):
    numbers = os.urandom(length)
    return ''.join(str(b%10) for b in numbers)
    
text = randomnumbers(length=10)  
hashing = hashlib.sha256(text.encode()).hexdigest()
print(f"text: {text} >>> \n {hashing}")