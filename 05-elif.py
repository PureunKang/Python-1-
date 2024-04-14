'''
#elif(else if)문
조건식이 여러개인 경우 사용
elif문은 여러개 사용 가능

#if - elif - else
    if 조건식A:
        (조건식A가 참이면 실행)
        실행문..
    elif 조건식B:
        (조건식A가 거짓이고 B가 참이면 실행)
        실행문..
    elif 조건식C:
        (조건식A, 조건식B가 거짓이고, C가 참이면 실행)
        실행문..
    ...
    else: #사용하고 싶다면 맨마지막에 들어갈 수 있음.
        (위의 모든 조건식들이 거짓이면 실행)
        실행문....
'''

subject = ''
if subject =='art':
    print('그림을 그립니다.')
elif subject == 'music':
    print('노래를 부릅니다.')
elif subject=='sports':
    print('공을 찹니다.')
else:
    print('개설된 과목이 아닙니다.')

# practice
score = int(input('점수 입력: '))
if score >=90:
    print('A')
elif score >= 80 #and score <90: / 이건 위에서 이미 거짓이 걸러졌으므로 적을 필요 없는 것임.
    print('B')
elif score >= 70 and score <80:
    print('C')
elif score >=60 and score <70:
    print('D')
else score <60:
    print('F')

