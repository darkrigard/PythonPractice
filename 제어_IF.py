# 제어 if문

# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."

pocket = ['money','mobile phone','paper']

if 'money' not in pocket:
    print("you need to take a taxi")
else:
    print("you need to walk")

# "주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라."

pocket = ['money','mobile phone','paper']

if 'dog' in pocket:
    pass
else:
    print("you should pay credit card")

# "주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라."

pocket = ['paper', 'handphone']
card = False

if 'money' in pocket: print("택시타고가")
elif card: print("택시타고가")
else: print("걸어가")

# 위 코드는 score가 60 이상일 경우 message에 문자열 "success"를, 아닐 경우에는 "failure"를 대입하는 코드이다.

# 파이썬의 조건부 표현식(conditional expression)을 사용하면 위 코드를 다음과 같이 간단히 표현할 수 있다.

# message = "success" if score >= 60 else "failure"
