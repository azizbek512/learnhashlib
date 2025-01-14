# "testdata" hash natijasining uzunligini hisoblang.
import hashlib
import sys # for knowing size of hash text
text = "testdata"
hash_text = hashlib.sha256(text.encode()).hexdigest()
lengthofhash = len(hash_text)
size = sys.getsizeof(hash_text)
print(f"text: {text}; \n hash text: {hash_text}; \n length of hash: {lengthofhash}; \n size of hash: {size}")
