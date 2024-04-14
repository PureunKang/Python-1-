'''
# if 조건문
조건식의 결과가 참이면 내부 실행문들을 수행
        if 조건식:
            실행문1
            실행문2

'''
num = -10
if num >0: # if 조건식:
    # 조건식이 참일 경우 실행할 공간
    # 조건식이 거짓이면 실행x
    print('조건문이 참입니다.')
    print('num은 양수입니다.')
print('조건문 끝나고 실행하는 문장') #조건문과 상관없이 실행하는 문장, 조건문 바깥에 있음.

n = 10
if n >=50:
    print('50보다 크거나 같습니다.')
if n < 50:
    print('50보다 작습니다.')