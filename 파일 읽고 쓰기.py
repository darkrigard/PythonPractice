f = open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'w')

for i in range(1,11):
    data = "%d번째 줄입니다. \n" %i
    f.write(data)

f.close()

f = open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'r')

line = f.readline()
print(line)

f.close()

f = open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()

f = open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'r')

lines = f.readlines()
for line in lines:
    line = line.strip()   # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)

f.close()

# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트를 리턴한다

f = open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'r')

data = f.read()

print(data)

f.close()

f = open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'a')

for i in range(11,20):
    data = "%d번째 줄입니다. \n"%i
    f.write(data)

f.close()

# 추가모드 'a'
with open("/Users/woojinchoi/Desktop/PythonPractice/새파일.txt", 'w') as f:
    
    f.write("Life is too short, you need python")

# 위와 같이 with문을 사용하면 with 블록(with 문에 속해있는 문장)을 벗어나는 순간 열린 파일 객체 f가 자동으로 close된다.
