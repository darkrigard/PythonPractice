# {키:벨류,키:벨류}

dic = {"name":"woojin", "phone":"01040798862", "birth":"19900901"}

a = {1:'a'}

a[2] = 'b'

print(a)

a['name'] = 'pey'

print(a)

a[3] = 'woojin'

print(a)

# del a[1]

print(a)

# del a[3]

print(a)

grade = {'pey':10, 'Julliet':99}

print(grade['pey'])

# # 키값에 리스트를 쓸수 없다 리스트는 변동가능성있음 고로, 튜플만 가능

print(grade['Julliet'])


for k in dic.keys():
    print(k)

print(list(dic.keys()))
# 리스트로 리턴값을 받고 싶은경우

print(dic.values())

print(dic.items())

print(dic.get('name'))

print(dic.get(3))

print(dic.get('foo', 'bar'))
# get을 쓸경우 키값이 없을때 오류가 나지않음 none값을 반환함, 좀 더 안전한 방법

# 키값이 없을경우 뒤 값이 디폴트로 출력됨

print('name'in dic)

print('emal'in dic)

