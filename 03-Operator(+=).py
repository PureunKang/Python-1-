'''
# 복합 대입 연산자 (사칙연산자+대입연산자)
+=. -=. *=, /=, %=. **=
제어문(조건문, 반복문)에서 자주 사용


'''
a = 100

a += 10 # a = a + 10 / 오른쪽의 값을 본인값에 대입!
print(a)

a -= 10 # a = a - 10
print(a)

a *= 5
print(a)

a //= 50 #/ 소수로출력됨
print(a)

a %= 4
print(a)

a **=3
print(a)
print('='*20)

#+= 연산
num1 = 100
num1 += 10
num1 += 20
print('num1: ', num1)

#-= 연산
num2 = 30
num2 -= 30
num2 -= 30
num2 -= 30
print('num2: ', num2)

# 1~10까지의 수 더하기 (누적합)
sum = 0 #더한값을 담을 그릇을 준비해야 함
for i in range(1,11):
    sum +=i
    print(i, '번재 sum:', sum) #과정알아보기 위해 넣은 출력문.
print('총합: ', sum)

# 1~10까지 짝수들의 합 구하기
sum = 0
for i in range(1,11):
    if i%2==0:
        sum +=i
print('짝수합: ', sum)

# 1~250까지 13의 배수 개수 구하기 (갯수 구하기)
count = 0 #갯수를 셀 변수
for i in range(1,251):
    if i%13==0:
        count+=1
print('13의 배수의 갯수: ', count)