a = [1,2,3,['a','b','c']]

print(a[-1])

print(a[0]+a[1])

print(a[-1][0])

b = [1,2,['a','b',['Life','is']]]

print(b[2][2][0])

c = [1,2,3,4,5]

print(c.sort())

print(c[0:2])

print(c[:4])

print(c[1:3])

print(b[2][:2])

d = [1,2,3]

e = [4,5,6]

print(d+e)

print(d*2)

print(len(d))

c[2] = 7

print(c)

del c[2]

del c[:2]

print(c)

c.append(7)

c.append([1,2])

c.reverse()

print(c.index(4))

print(c)

c.insert(0,0)

print(c)

c.insert(5, 10)

print(c)

c.remove(4)

print(c)

c.pop()

print(c)

print(c.count(5))

c.extend([2,20,30,24,58,19])

print(c)

