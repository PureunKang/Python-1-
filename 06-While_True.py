'''
# while 무한루프 형태
조건식을 참으로 시작하여 반복문 무한 실행
반복을 멈추려면 조건문과 break 명령문이 필요

    while True:
        반복문
        if 조건식:
            break

# break 키워드
반복문을 빠져나옴. 탈출(exit)
조건문과 함께 사용

# continue 키워드
반복문 처음으로 돌아감
continue 다음줄부터의 실행문은 스킵
'''

# 1~5 반복
k = 1
while True:
    print(k)
    k+=1
    if k==6:
        break

# 1~20사이 짝수 출력
a = 1
while True:
    if a%2==0:
        print(a, end=" ")
    a+=1
    if a==21: #끝값, 항상 주의 할 것.
        break
print()
print('='*10)

#== 입력 받아서 while문 탈출하기 ==#
# 'Q' 를 입력하면 무한반복 종료
while True:
    print('반복을 멈추려면 Q를 입력하세요')
    a = input('입력: ')
    if a=='Q':
        break
print()
print('='*10)

# 숫자 -1을 입력하면 무한반복 종료
while True:
    num = int(input('숫자 입력(종료는 -1): '))
    if num==-1:
        print('프로그램을 종료합니다.')
        break
print()

# continue문 사용
# 1~20 사이 5의 배수를 제외하고 출력
i = 0
while i<20:
    i+=1
    if i%5 ==0:
        continue #참인 경우, 그냥 while로 돌아감. 그 아래 print로 안 가고.
    print(i, end = ' ')

