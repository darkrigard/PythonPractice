# 튜플은 요솟값 삭제, 변경 불가능

# 튜플 다루는건 리스트와 완전동일

# del t1[0]

# t1[0] = 'c'

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

t1 = (1,2,'a','b')

print(t1[0])

print(t1[3])

print(t1[:2])

print(t1[1:3])

t1 = (1,2, 'a', 'b')

t2 = (3,4)

print(t1+t2)

print(t2 * 3)

print(len(t2))

t6 = (4,)
print(t3 + t6 )