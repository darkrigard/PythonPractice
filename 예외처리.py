# try:
#   ...  
# except [발생오류 [as 오류변수]]:
#   ...  
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 
# 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

# try:
#     ...
# except 발생오류:
#     ...
# 이 경우는 오류가 발생했을 때 except문에 미리 정해 놓은 오류와 동일한 오류일 경우에만 
# except 블록을 수행한다는 뜻이다.

# try:
#     ...
# except 발생오류 as 오류변수:
#     ...
# 이 경우는 두 번째 경우에서 오류의 내용까지 알고 싶을 때 사용하는 방법이다.


# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# try:
#     무언가를 수행함.


# finally:
#     a.close() 중간에 오류가 발생하더라도 무조건 실행됨.


# 여러개 오류 처리
# try:

#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")


# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# try:

#     age = int(input('나이를 입력하세요: '))

# except:

#     print("입력이 정확하지 않습니다.")

# else:
#     if age <= 18:
#         print("미성년자는 출입금지입니다.")

#     else:
#         print("환영합니다.")


# 오류회피

# try: 
#     f = open("없는파일", 'r')
# except FileExistsError:
#     pass


# # 오류 강제 발생

# class Bird:
#     def fly(self):
#         raise NotImplementedError 
# # 상속 자식들은 fly함수 있어야해!


# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagle = Eagle()

# eagle.fly


# 예외 만들기

class MyError(Exception):

    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


# say_nick("천사")
# say_nick('바보')


# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError:
#     print("허용되지 않는 별명입니다.")


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)