'''
# 모듈(module) - 파이썬 코드 파일
    import 모듈이름

모듈은 변수나 함수 또는 클래스 등의 파이썬 코드를 작성해 놓은 파일이다.
모든 코드들을 직접 만들어서 사용할 수 없기에,
많이 사용되거나 유용한 기능들을 미리 작성해둔 모듈을 가져와서 사용한다.

표준 모듈: 파이썬에 기본적으로 내장되어 있는 모듈
        math, random, datetime, time, sys...

외부 모듈: 다른 사람들이 만들어서 배포한 모듈. 추가 다운 필요
        numpy, pandas, beautifulsoup,..
'''
# 1. math 모듈
import math
print(math.pi) #math 페이지에 있는 pi 변수를 출력한다.
print(math.e)
PI = math.pi #상수는 대문자로 보통 씀. 물론 파이썬은 그러지않지만..그냥..
print(math.sin(PI/2))
print(math.cos(PI/2))
print(math.floor(PI)) #내림
print(math.ceil(PI)) #올림
print(round(3.14)) #반올림. 기본제공함수.
print()

# cf) 기본제공 함수 (import 할 필요없이 바로 사용 할 수 있는 거)
nums = [1,2,3,4,5]
print(sum(nums))
print(len(nums))
print(max(nums))
print(abs(-10)) #절대값
print()

# from 모듈명 import * (불러오기 필요없이 바로 사용 가능함)
from math import *
print(sin(PI/2))

# 2. random
import random as rd # as 별칭
print(rd.random())
print(rd.uniform(10,15)) # 해당 범위 랜덤한 실수 리턴
print(rd.randrange(1,5, 2)) # 랜덤 정수 리턴 (이상, 미만, 증감값)
print(rd.randint(1, 45)) # 랜덤 정수 리턴 (이상, 이하) 증감값(스텝값)은 줄 수 없음

print(rd.sample([1,2,3,4,5], 2)) # [모집단], 표본갯수

# 로또 번호 생성하기
a = [i for i in range (1,46)]
# print(a)
lotto = rd.sample(a,6)
lotto.sort()
print('로또 번호:', lotto)

# 3. datetime 모듈
import datetime as dt
print(dt.datetime.now())
now = dt.datetime.now()
print(f'{now.year}년 {now.month}월 {now.day}일')
print()

# 4. time 모듈 (시간기능모듈)
import time as t
print('3초간 정지..')
t.sleep(3)
print('후 실행합니다.')



