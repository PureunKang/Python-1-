#== 문자열 관련 함수 ==#
a = 'My weekend'
print(len(a))

# 문자 개수 세기
print('문자열에서 e의 개수:', a.count('e'))

# 특정 문자 위치 찾기
print('문자열에서 y의 위치:', a.index('y'))
print('문자열에서 y의 위치:', a.find('y'))

# print('문자열에 없는 문자 찾을때:', a.index('z'))
print('문자열에 없는 문자 찾을때:', a.find('z')) #없는 걸 확인하며 계속 진행하고 싶을 때
print()

# 공백 제거하기
k = ' spring '
print(f'원본: ({k})')
print(f'양옆 공백 제거: ({k.strip()})')
print(f'왼쪽 공백 제거: ({k.lstrip()})')
print(f'오른쪽 공백 제거: ({k.rstrip()})')

s= '**밤*하늘의별***'
print('별표 제거:', s.strip('*'))
print()

# 문자열 바꾸기
w = 'It is spring'
next_w=w.replace('spring','summer')
print('문자열 바꾸기:', next_w)
s2 = s.replace('*','') # 문자열에서 특정 문자 제거
print(s2)

# 문자열 나누기
k = 'Summer is coming'
print('\n문자열 나누기:', k.split())
a = k.split()
print(a[0], type(a), len(a))

date = '2024-04-07'
print('날짜 기호 기준으로 나누기:', date.split('-'))
print('연도:', date.split('-')[0])

phone = '010-1234-5678'
print('핸드폰 번호 뒷자리:', phone.split('-')[-1])




