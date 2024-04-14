'''
# 인덱싱과 슬라이싱
happy = 'My weekend'
index : [0123456789]

인덱싱 (indexing): 가리킨다. 특정 위치(번호)의 데이터를 추출한다. [3]
슬라이싱(slicing): 잘라낸다. 특정 범위의 데이터들을 추출한다. [2:5]

# [a:b] a이상 b미만
a,b는 정수만 가능


'''
happy = 'My weekend'

# 문자열 인덱싱
print(happy[0]) # 첫번째 문자 추출
print(happy[1])
print(happy[3] + happy[4])
print(happy[-1]) # 끝에서 첫번째 문자 추출
print(happy[-3]+happy[-2]+happy[-1])
print()

#문자열 슬라이싱
print(happy[0:2])
print(happy[:2]) # 처음부터 2번 인덱스 전까지 선택
print(happy[7:10])
print(happy[7:]) # 7번 인덱스부터 끝까지 선택
print(happy[:]) # 전체선택
print(happy[-3:]) #끝에서 3번째부터 끝까지