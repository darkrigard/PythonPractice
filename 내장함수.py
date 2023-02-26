print(abs(3))

print(abs(-3))

print(all([1,2,3]))

print(all([1,2,3,0]))

for i, name in enumerate(['body','foo','bar']):
    print(i, name)

# def positive(l):
#     result = []
#     for i in l:
#         if i > 0:
#             result.append(i)
#     return result

def positive(x):
    return x > 0

# print(positive([1,-3,2,0,-5,6]))

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(len("python"))

print(list("python"))

def two_times(x):
    return x*2

print(list(map(two_times, [1,2,3,4])))

print(max([1,2,3]))

print(min([4,5,6]))

print(list(range(5,10)))

print(list(range(5,10,2)))

print(round(10.7))

print(sorted([1,10,8,4,6,3,22]))

print(sum([1,2,3]))

print(tuple("abc"))