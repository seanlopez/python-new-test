import hashlib

m = hashlib.md5(b"cisco")

psw = m.hexdigest()

print(psw)

m.update(b"passwd")

psw = m.hexdigest()

print(psw)
