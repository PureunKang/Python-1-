numA = float(input('점수1 입력: '))
numB = float(input('점수2 입력: '))
numC = float(input('점수3 입력: '))
average = (numA+numB+numC)/3
if average >= 80:
    res = '합격'
else:
    print('결과: 불합격')
    res = '불합격'
print('결과:', res)
