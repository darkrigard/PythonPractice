# 모듈을 저장한 디렉터리로 이동하지 않고 모듈을 불러와서 사용하는 방법

import sys

sys.path.append("/Users/woojinchoi/Desktop/PythonPractice/mymod")

sys.path


import mod2

print(mod2.add(3,4))

