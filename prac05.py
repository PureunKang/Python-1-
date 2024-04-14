x = int(input('시작숫자 입력: '))
y = int(input('종료숫자 입력: '))
sum = 0
for i in range(x,y+1):
    if i%4==0:
       sum +=i
print(x,'부터 ', y,'까지의 4의 배수들의 합은 ', sum, sep='')
print(f'{x}부터 {y}까지의 4의 배수들의 합은 {sum}')
