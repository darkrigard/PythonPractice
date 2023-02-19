
class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second

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

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


# a = FourCal(5,10)

# print(a.first)
# # a.setdata(4,2)

# print(a.add())

# print(a.mul())

# print(a.sub())

# print(a.div())

# a = MoreFourCal(4,2)

# print(a.pow())

# a = FourCal(4,0)

# print(a.div())

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0

        else:
            return self.first / self.second

# b = SafeFourCal(4,0)

# print(b.div())

class Family:
    lastname = "김"


print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

a.lastname = "최"

print(a.lastname)

print(Family.lastname)