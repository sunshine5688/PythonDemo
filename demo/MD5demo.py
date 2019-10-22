import hashlib
#import md5 #Python2里的引用
s='d2c0bba3abec1ce19358dbb75f97607d'
print(s[5:21])
# s.encode()#变成bytes类型才能加密
m= hashlib.md5(s.encode())
print(m.hexdigest()[5:21])



m=hashlib.sha3_224(s.encode()) #长度是224
print(m.hexdigest())

m=hashlib.sha3_256(s.encode())  #长度是256
print(m.hexdigest())

m=hashlib.sha3_512(s.encode()) #长度是512
print(m.hexdigest())