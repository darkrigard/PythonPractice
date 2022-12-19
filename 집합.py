s1 = set([1,2,3])
# 괄호안에 리스트나 문자을 넣어서 만듬

print(s1)

s2 = set("Hello")
# 괄호안에 리스트나 문자을 넣어서 만듬

s3 = set(["bongdu", "chuljin"])

print(s2)
# 중복을 허용하지않는다. 순서가 없다, 고로 인덱싱으로 값을 얻을수 없다.

print(s3)

l1 = list(s1)

print(l1[0])


t1 = tuple(s1)

print(t1[1])

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2) 
# 교집합

print(s1 | s2)
# 합집합

print(s1 - s2)
# 차집합

s1.add(7)
# 값 한개 추가하기

print(s1)

s1.update([10,20,30])
# 값 여러개 추가하기

print(s1)

s1.remove(20)

print(s1)