sum = 0
while True:
    num = int(input('정수 입력: '))
    sum += num
    if num == 0:
        break
print('합계: ', sum)