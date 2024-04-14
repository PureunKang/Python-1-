#== 출력문 옵션 알아보기 ==#
# seperator: (,)사이 출력할 데이터들을 sep='내용'으로 연결
print(2,0,2,4) #콤마가 곧 빈칸이 됨
print(2,0,2,4, sep=' ') # sep=' '이 기본값(defalt값). 그래서 라인3랑 동일내용 출력됨.
print(2,0,2,4, sep='') #=> 이게 가장 많이 사용하는 용도임. 공백없ㅇㅐ기
print('2024','03','16', sep='')
print('시험 난이도: toefl', 'toeic', sep='>>>')
print('123+456',123+456, sep='=')
print()


# end: 문자열의 마지막을 end='내용'으로 출력
print('원주율:', 3.141)
print(592)

print('원주율:', 3.141, end='\n') #위 라인과 동일함. end=\n(줄바꿈)이 기본값.
print(592)

print()
print('원주율:', 3.141, end='')
print(592)
print()

print('3월 4월 5월', end="")
print('6월 7월 8월')

print('3월 4월 5월', end="")
print()
print('6월 7월 8월')
print()

# sep, end 함께 사용하기
print(15,27, sep='+', end="=")
print(15+27)

