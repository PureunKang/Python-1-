#이중for문 q1
for i in range (1,6): #i번째줄
    for j in range(1,i+1): # 별을 각 줄에 5개씩 생성 #==for j in range(i)
        print('*', end='')
    print()



# 문자열*숫자
for i in range(1,6):
    print('*'*i)



# q2 / 아래처럼 일반식을 먼저 세우기.
# for i in ~ : i 번쨰줄
# for 빈칸: 4 3 2 1 0 # (5-i)개
# for 별표: 1 2 3 4 5 #i 번쨰줄에서 i개

for i in range (1,6): #i번째줄
    for j in range(5-i):
        print(' ', end='')
    for k in range (1,i+1):
        print('*', end='')
    print()

'''
알고리즘 트레이닝 사이트
백준
프로그래머스
코드업
'''