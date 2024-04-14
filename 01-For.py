'''
# for 반복문
for문은 코드 실행을 정해진 횟수만큼 반복할 때 사용한다.

#for문의 일반적인 형태
    for 반복변수 (i,j,k, etc) in 범위:
        반복문..
###############################################
# for문과 range()
    for i in range(a, b):
        반복문..
1. a부터 (b-1)까지 반복
2. range (시작값, 끝값)
3. i의 범위: a <= i < b
##############################################
    for i in range(b):
        반복문..
    1. b번 반복
    2. range(끝값)
    3. i의 범위: 0 <= i < b
##############################################
    for i in range(a, b, n):
        반복문..
    1. a 부터 (b-1)까지 n만큼 건너뛰며 반복
    2. range(시작값(start), 끝값(end), 증감값(step))
    3. a, b, n은 정수만 가능
'''
#=== for i in range(a, b) ==#
# 0~4까지 5번 반복
for i in range(0,5):
    print(i)

# 1~10까지 숫자 출력
for i in range(1,11):
    print(i)

# 4~7까지 숫자 한줄로 출력
for i in range(4, 8):
    print(i, end=' ') #end='' 공백없으면 띄어쓰기 없이 숫자들 붙어있을거임.

print() #end 옵션 해제
print('='*10) #=print('==================')

# == for i in range(b): ==#
# 0~4까지 5번 반복
for i in range(5):
    print(i)

# '일요일' 4번 출력하기
for i in range(4):
    print('일요일')

# '=' 기호 10개 한줄로 출력해보기
for k in range(10):
    print('=', end="")
print()

#== for i in range(a, b, n): ==#
# 1~10 범위에서 숫자 2씩 건너뛰면서 출력
for i in range (1,11, 2):
    print(i, end=' ')
print()
# 1~40 사이 3의 배수만 한줄로 출력
for i in range(3, 40, 3):
    print(i, end=' ')
print()

# 10~1 범위에서 숫자 2씩 감소하면서 한줄로 출력
for i in range(10, 1, -2):
    print(i, end=' ')
print()

# '카운트다운' 5~1까지 출력
for i in range(5,0, -1):
    print('카운트다운',i)
