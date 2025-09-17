import hashlib

hashvalue=input("enter ")

haobj1=hashlib.md5()
haobj1.update(hashvalue.encode())
print(haobj1.hexdigest())

haobj2=hashlib.sha1()
haobj2.update(hashvalue.encode())
print(haobj2.hexdigest())


haobj3=hashlib.sha224()
haobj3.update(hashvalue.encode())
print(haobj3.hexdigest())

haobj4=hashlib.sha256()
haobj4.update(hashvalue.encode())
print(haobj4.hexdigest())