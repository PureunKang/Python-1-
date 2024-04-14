'''
# return문
    def 함수명(매개변수..):
        ...
        return 리턴값

함수를 선언 할 때 return문의 작성 유무에 반환값의 존재 여부를 선택 가능하다.
'''
# 함수 선언
def get_add(x, y):
    return x+y

# 함수 호출
print(get_add(10, 20))

# 두 실수의 합을 반환
num = get_add(1.5, 3.7)
print(num, type(num))

# 두 문자열을 이어붙여서 반환
msg =get_add('장마담', '사쿠라여')
print(msg,type(msg))
##################################
def get_avg(a,b,c):
    sum = a+b+c
    return sum/3
print('평균은', get_avg(15,15,30))
##############################################
def good_day():
    return '좋은 하루 보내세요!'
print(good_day())

