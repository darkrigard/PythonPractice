# a = 123

# b = 3

# a = 5

# c = 1.4

# print(a + c)

# print(a * b)

# # print(a ** b) 거듭제곱

# # print(a % b) 나머지 반환

# # print(7 // 4) 몫 반환

# print(14 % 3)


# food = "Python's favorite food is perl"

# print(food)

# say = '"Python is very easy" he says'

# print(say)

# say1 = "\" Python is very easy. \" he says"

# print(say1)

# multiline = "Life is too short\nYou need python"

# print(multiline)

# multiline1 = '''Life is too short
# You need python'''

# print(multiline1)

# say2 = "i will python\nkeep going"

# say3 = '''i want hope doing well
# in Python'''

# print(say2)
# print(say3)

# head = "Python"

# tail = "is fun!"

# print(head + tail)

# a = "python"

# print(a * 2)

# print("=" * 50)
# print("multistring test")
# print("=" * 50)

# print(len(a))


a = "Life is too short, You need Python"

print(a[3])

print(a[12])

# print(a[-1]) //역방향

print(a[-2])

b = a[0] + a[1] + a[2] + a[3]

c = a[5:7]

print(b)

print(c)

print(a[19:])

print(a[19:-7])

Fullday = "20010331Rainy"

year = Fullday[:4]

date = Fullday[4:8]

weather = Fullday[8:]

print(year)
print(date)
print(weather)

Change = "20221218" + Fullday[8:]

print(Change)

print("i eat %d apples" %3)

print("i eat %s" % "apple")

number = 3
day = 10
print("i eat %d apples. so i was sick for %s days" %(number, day))

print("error is %d%%" %98)