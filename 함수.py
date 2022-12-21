# 함수

def add(a,b):
    return a + b


a = 3

b = 10

c = add(a,b)

print(c)

def add(a,b):
    result = a + b
    return result

a = add(3,4)

print(a)

def say ():

    return 'Hi'

a = say()

print(a)

def add(a, b):

    print("%d, %d의 합은 %d입니다." % (a, b, a+b))


a = add(3,4)

print(a)

def say():
    print('HI')

say()

def sub(a, b):
    return a - b

result = sub(a = 7, b = 3)

print(result)

# args는 통상적으로 많이 사용함 arguments의 약자
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1,2,3)

print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)

print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result



result = add_mul('add', 1,2,3,4,5,6,7,8)

print(result)

result = add_mul('mul', 1,2,3,4,5,6,7,8,9,10)

print(result)
# 딕셔너리 형태로 바꿔준다.
def print_kwargs(**kwargs):
    print(kwargs) 



print_kwargs(a = 1)
print_kwargs(name = "foo")
print_kwargs(year = 15)
print_kwargs(grade = 3)


def add_and_mul(a,b):
    return a+b, a*b

result = add_and_mul(3,4)

print(result)


result1, result2 = add_and_mul(4,5)

print(result1)
print(result2)

def say_nick(nick):

    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)


say_nick('바보')
# 매개변수 호출시 순서주의
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." %age)
    
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("quency", 14, True)

say_myself("doli", 20, False)

a = 1 
def vartest(a): 
    a = a +1 
    return a

a = vartest(a)
print(a)

# 함수영역 바깥의 변수에 접근이 가능하지만 되도록 쓰지 않는걸 추천
a = 1 
def vartest(): 
    global a 
    a = a+1

vartest() 
# 람다식 간단한 함수 만들때 사용하면 메모리 절약에 효과적
add = lambda a, b: a+b
result = add(3, 4)
print(result)
