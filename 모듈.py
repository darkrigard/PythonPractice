# 반드시 같은 디렉토리에 있어야함

# import mod1

# print(mod1.add(3,4))

# print(mod1.sub(4,2))

# mod1.add, mod1.sub처럼 쓰지 않고 
# add, sub처럼 모듈 이름 없이 함수 이름만 쓰고 싶은 경우

#from mod1 import add, sub # from mod1 import *

# print(add(3,4))
# print(sub(7,2))


import mod1

a = mod1.Math()
print(a.solv(2))

print(mod1.add(mod1.PI, 4.4))