'''
# 중첩 조건문
if문 안에 새로운 if문을 추가
중첩조건문 vs 논리연산자

'''
age =16
cm = 170

# 중첩 조건문
if age>=14:
    if cm>=160: #뼈대만 만들고 싶을 때 이 부분에 pass 쓰고 넘어가서 다른 조건식쓰기!
        print('번지점프 가능')
    elif cm>=140:
        print('락스핀 가능')
    else:
        print('롤러코스터 탑승 가능')
else:
    print('회전목마 올라가자')

#논리연산자를 사용한 조건문
if age >=14 and cm>=160:
    print('번지점프 가능')
elif age>=14 and cm>=140:
    print('락스핀 가능')
elif age>=14:
    print('롤러코스터 탑승 가능')
else:
    print('회전목마 올라가자')
