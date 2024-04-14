'''
중첩 반복문
    for i in range(a,b): #외부 for문
        반복문A
        for j in range(c,d): #내부 for문
            반복문B
        반복문C

실행 순서
    외부 for문에 진입하면
        반복문A를 먼저 수행하고
        내부 for문에 진입하여 반복문B를 반복 수행하고,
        반복문C를 수행한 후
    다시 외부 for문 처음으로 돌아가서 반복을 진행
'''
# 이중 for문
for i in range(1, 6):
    for j in range (1,4):
        print(f'i ={i} | j = {j}')

print('#'*20)
#3단 출력하기
for j in range(1,10):
   print(f'{3} x {j} = {3*j}')
print('#' * 20)

#구구단 출력하기 1
for i in range(2,10): #2단~9단 범위
    print(f'{i}단')
    for j in range(1, 10):
        print(f'{i} x {j} = {i * j}')
    print('='*20)

#구구단 출력하기 2
for i in range(2,10):
    print(f'\n{i}단: ', end=' ')
    for j in range(1, 10):
        print(i * j, end=' ')
    #\n쓰는 대신 이 라인에다가 print() 추가하면 엔터 할 수 있음.