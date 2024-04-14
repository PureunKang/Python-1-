'''
# 딕셔너리(Dictionary)
딕셔너리이름 = {key:value, key:value..}
딕셔너리 특징: 순서x, key중복x, 변경o

'''
a ={'name': '너구리', 'birth': '5/1', 'age':10}
b ={0: 'today', 2:'is', 1:'sunday'}
c = {1:20, 2:40, 3:60}
d = {'num1':100, 'num':200}
e = {'cute':['dog', 'cat'], 'wild':('tiger', 'lion')}

print('딕션너리 a길이: ', len(a))
print('딕셔너리 e길이:', len(e))

# key값으로 value값 접근
print(a['name'])
print(b[2]) #2번 인덱스가 아닌 2번 키값 찾는 것임!!
print(c[3])
print(d['num1'])
print(e['cute'][0])
print()

# 딕셔너리 데이터 추가, 수정, 삭제
a['hobby']  = 'YouTube' #딕셔너리명[새로운key] = value
print(a)
c[4] = 80
print(c)
print('='*30)
a['name'] = 'nuguri' #기존 key에 value 대입하여 수정
print(a)

del a['hobby'] #해당 key와 value를 삭제
print(a)
del c[4]
print(c)
print('='*30)

#== 딕셔너리 key, value 가져오기 ==#
# key값 가져오기
print(a.keys())
print(b.keys())
print(list(a.keys()))

# value값 가져오기
print((a.values()))
print(list(a.values()))

# key, value 쌍으로 가져오기
print(a.items())
print(list(a.items()))
print('='*40)

# 딕셔너리 key 중복일때
f = {'a': 1, 'a': 2}
print(f)

g = {'a': 1, 'b': 2}
print(g)

# 딕셔너리에 없는 key 를 찾을 때
# print(g['c']) # 에러
print(g['a'],g.get('a'))
print(g.get('c')) # get으로 없는 거 찾을 때 없다고 알려준다.