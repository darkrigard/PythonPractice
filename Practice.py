class FourCal:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        if self.second == 0:
            return 0
        
        else:
            result = self.first / self.second
            return result
    def mul(self):
        result = self.first * self.second
        return result

class MoreFourCal(FourCal):

    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(MoreFourCal):

    def mul(self):
        if self.first > 100:
            return "숫자가 너무 큽니다."
        else:
            result = self.first * self.second
            return result
        

a = SafeFourCal(101, 6)

print(a.add())

print(a.div())

print(a.mul())

print(a.sub())

print(a.pow())


