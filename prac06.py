num = int(input('팩토리얼 입력: '))
mul = 1
for i in range (1, num+1): #(num,0,-1)
    mul *= i
print(f'{num}!={mul}')
