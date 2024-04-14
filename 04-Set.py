'''
# 집합 (set)
집합이름 = {데이터, 데이터, 데이터, ..}
집합 특징: 순서x, 중복x, 변경o


'''
a = {10, 20, 30, 20, 10}
b = {'How', 'was', 'your', 'day'}
c = set('sakura')

print(a, type(a), len(a)) # 숫자는 출력할때 오름차순
print(b) # 순서 일정x, 출력할 때마다 순서 계속 바뀜
print(c)
print()

# 집합 데이터 추가, 삭제
s = {1,2,3}
s.add(4)
print(s)
s.update([5,6,7]) #대괄호, 소괄호 , 중괄호에 담아서 더하면 됨. (리스트, 튜플 등 상관x)
print(s)
s.remove(2)
print(s)
print()

# 교집합, 합집합, 차집합
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print('교집합: ', s1 & s2) #and
print('합집합: ', s1 | s2) #or
print('차집합:', s1 - s2)

# 비트연산자
print(1&1)
print(1&0)
print(1|0)

# 비어 있는 집합 만들기
k ={} #딕셔너리로 인식함.
print(k, type(k))


k = set() #비어있는 집합 생성
print(k, type(k))
k.add(10)
print(k)