import hashlib


python_program = """for i in range(10):
    print(i)"""
    
print(python_program)
# for b in python_program.encode('utf-8'):
#     print(b, chr(b))
original_hash = hashlib.sha256(python_program.encode('utf-8'))
print(original_hash)
print(original_hash.hexdigest())