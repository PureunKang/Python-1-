#== 문자열 포맷팅 ==#
# '{}'.format(): 포맷 함수를 사용한 포맷팅
print('사과 {}개 주세요')
print('사과 {}개 주세요'.format(5))
num = 3
print('참외 {}개 주세요'.format(num))
print('지불하실 {}은 총 {}{}입니다.'.format('금액', '$', 100))
print('내가 {0} 기린 {1}은 너가 {0} 기린 {1}보다 잘 그렸다.'.format('그림','그림'))
print('제 이름은 {name}이며 {age}세 입니다.'.format(age=10, name='너구리'))

msg ='어제는 {}의 날이었습니다.'.format('강아지') #print옵션 아닌 문자열 기능인 점 기억할것 !!
print(msg)

# f'{}' : f문자열 포맷팅
season = '봄'
print(f'현재 계절은 {season}입니다.')

a = 10
b = 20
print(f'{a} + {b} = {a+b}')

pi = 3.141592
print(f'{pi:0.2f}') #{} 내 f는 float 뜻함 / 즉, 소수점 2자리까지 표현

price = 12000
print(f'{price:,}원') #천단위 콤마 표현

name ='오리'
age = 5
msg =f'제 이름은 {name}이며 {age}세 입니다.'
print(msg)
print()

# %d (decimal, 10진법), %s: 포맷 코드를 사용한 포맷팅
print('오늘은 %d일 입니다.'% 24.5) #%d: 정수만 표현한다.
print('체온은 %f도 입니다.' % 36.5) #%f: 실수
print('PI = %.2f' % 3.141592) # %.표현자리수
print('오늘은 %d년 %d월 입니다.' %(2024,3))
print('다음 계절은 %s입니다.'% '여름') #%s: 문자열
print('이니셜은 %c입니다.' % 'D') #%c: 단일 문자