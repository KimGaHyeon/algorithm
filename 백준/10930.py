# https://www.acmicpc.net/problem/10930
import hashlib
HASH_NAME = "sha256"
txt = input("Enter the text to convert: ")
text = txt.encode('utf-8')
md5 = hashlib.new(HASH_NAME)
md5.update(text)
result = md5.hexdigest()
print(result)
