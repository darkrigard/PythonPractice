# class Calculator:

#     def __init__(self):
#         self.result = 0

    
#     def add(self, num):
#         self.result += num
#         return self.result

#     def sub(self, num):
#         self.result -= num
#         return self.result


# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

class FourCal:

    def __init(self, first, second):
        self.first = first
        self.second = second

# 이렇게 객체에 first, second와 같은 초깃값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다. 
# 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
# 파이썬 메서드 이름으로 __init__를 사용하면 이 메서드는 생성자가 된다. 다음과 같이 FourCal 클래스에 생성자를 추가해 보자.
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# setdata 메서드에는 self, first, second 총 3개의 매개변수가 필요한데 실제로는 a.setdata(4, 2)처럼 2개 값만 전달했다.
# 그 이유는 a.setdata(4, 2)처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는 setdata메서드를 호출한 객체 a가 자동으로 전달되기 때문이다. 
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다. 객체를 호출할 때 호출한 객체 자신이 전달되기 때문에 self라는 이름를 사용한 것이다. 
# 물론 self말고 다른 이름을 사용해도 상관없다. 메서드의 첫 번째 매개변수 self를 명시적으로 구현하는 것은 파이썬만의 독특한 특징이다. 예를 들어 자바 같은 언어는 첫 번째 매개변수 self가 필요없다.

class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):

    def div(self):
        if self.second == 0:
            return 0

        else:
            return self.first / self.second

a = FourCal()

a.setdata(4, 2)

print(a.first)

print(a.add())

print(a.mul())

print(a.sub())

print(a.div())

b = MoreFourCal()

b.setdata(4,2)

print(b.pow())

c = SafeFourCal()

c.setdata(4,0)

print(c.div())





