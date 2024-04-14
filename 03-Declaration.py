'''함수 선언하기 (function declaration)
# 함수 입출력 흐름
(입력) -> 함수 -> (결과)
(매개변수) -> 함수 -> (리턴값)

# 함수 구성 경우의수
리턴값 매개변수 함수선언: 나중에는 내가 판단해서 설정 해야 함
x     x       f(): ...
o     x       f(): ...return 0
x     o       f(a): ...
o     o       f(a): ...return 0

# 함수 만들기
1. 만들려는 함수의 기능을 결정한다.
2. 기능에 맞는 함수 이름을 정한다.
3. 리턴값(출력)과 매개변수(입력)를 고려하여 함수를 만든다.
4. 함수이름과 매개값을 일치시켜 함수를 호출한다.
'''

# 리턴값x, 매개변수x
# 예제1) "안녕하세요" 문자열을 5번 출력하는 함수를 만드시오.
def hello():
    for i in range(5):
        print('안녕하세요')
hello()

# 리턴값o, 매개변수x
# 예제2) "감사합니다' 문자열을 반환하는 함수를 만들고 출력문으로 확인하시오
def msg():
    return '감사합니다'
print(msg())

# 리턴값x, 매개변수o
# 예제3) 매개변수로 문자열과 숫자를 입력받고,
        #받은 숫자의 횟수만큼 받은 문자열 내용을 출력하는 함수를 작성하시오.
def repeat_msg_byNum(msg,num):
    for i in range(num):
        print(msg)
print(repeat_msg_byNum('감사합니다',5))
repeat_msg_byNum(msg='4월', num =6)
repeat_msg_byNum(num=2, msg='종강종강')

# 리턴값o, 매개변수o
# 예제4) 매개변수로 네 수를 입력 받고 평균값을 리턴하는 함수를 작성하시오.
def avg(a,b,c,d):
    return (a+b+c+d)/4
print(avg(15,15,15,30))

# 매개변수로 리스트를 입력받아서 평균값 리턴하는 함수
def average(a):
    return sum(a)/len(a)
k = [10, 20, 30]
print(average(k))
print(average([10,20,30,40]))


