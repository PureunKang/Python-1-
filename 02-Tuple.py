'''
# 튜플(Tuple)
튜플이름 = (데이터0, 데이터1, 데이터2, ...)
튜플 특징: 순서o, 중복o, 변경x

'''
a = (5,10, 15, 10, 5)
b = (5, 10, 'Sun', 'day', 'Morning')
c = (0, True, ('Sun', 'day','Morning'))

print('a =', a, type(a))

# 튜플 인덱싱
print(a[1], a[-2])
print(a[2], a[-3])
print(b[2]+b[3])
print(c[0]+c[1])
print(c[-1][-1])
print()

# 튜플 슬라이싱
print(a[2:])
print(b[0:5:2]) #2씩 건너띄며 선택하겠다 (시작, 끝값, 증감값)
print(b[::2])
print(c[2][::2])
print()
####################
d = (1,2,3,4,5)
e = (6,7,8)

f = d+e
print('f = ',f)
g = e*3
print('g= ', g)

# 튜플 데이터를 index로 찾기
print(g.index(7)) # 가장 앞에 있는 순서만 알려줌.
print(g.index(7,2)) #7이라는 데이터를 2번 인덱스부터 찾겠다.


