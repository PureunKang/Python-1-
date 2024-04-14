count = 0
while True:
    ment = input('문자를 입력하시오(종료는 . 입력): ')
    if ment == 'a':
        count +=1
    if ment =='.':
        break
print ('문자 a의 개수: ', count)