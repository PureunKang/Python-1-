'''
Q) 사용자로부터 두 개의 정수를 입력받고,
    4개의 함수 중에서 선택하여 실행시켜
    두 수의 연산 결과를 나타내시오.
    함수명: add, sub, mul, div
    매개변수: 정수형 2개
    리턴값: 정수형 1개

    <실행화면1>
    정수1 입력: 10
    정수2 입력: 20
    -------------
    두 수의 연산 선택
    1. 합
    2. 차
    3. 곱

     <실행화면2>
    정수1 입력: 10
    정수2 입력: 20
    --------------
    두 수의 연산 선택
    1. 합
    2; 차
    3. 곱
    4. 나눗셈
    ---------------
    연산을 선택하시오: 3
    연산 결과: 200
'''
# 함수 선언
def add(x, y): return x+y
def sub(x, y):
    if x>y:
        return x-y
    else:
        return y-x
def mul(x,y): return x*y
def div(x,y):
    if x>y:
        return x/y
    else:
        return y/x
# 입력문
num1 = int(input('정수1 입력: '))
num2 = int(input('정수2 입력: '))
# 연산 선택
print('두 수의 연산 선택', '1. 합', '2. 차', '3. 곱', '4. 나눗셈')
# 입력문
msg = int(input('연산을 선택하시오:'))
# 조건문
if msg ==1:
    res = add(num1, num2)
elif msg == 2:
    res = sub(num1, num2)
elif msg == 3:
    res = mul(num1, num2)
elif msg == 4:
    res = div(num1, num2)
# 함수 실행
print('연산 결과:', res)


# 심화) 딕셔너리를 이용하여 함수 선택하기
select = {1: add, 2: sub, 3: mul, 4: div}
f = select[msg] #f가 곧 함수가 된 것임.
print('연산 결과:',f(num1, num2))



