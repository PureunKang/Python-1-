num1 = int(input('input number1:'))
num2 = int(input('input number2:'))
num3 = int(input('input number3:'))
if num1 > num2 and num1 > num3:
    print('가장 큰 수:', num1)
#elif num2 > num1 and num2 > num3:
    ##else:
    #print('가장 큰 수:', num3)
elif num2>=num3:
    print('가장 큰 수:', num2)
else:
    print('가장 큰 수:', num3)

#효율
num1 = int(input('input number1:'))
num2 = int(input('input number2:'))
num3 = int(input('input number3:'))
#중첩문 사용
if num1>=num2:
    if num1>=num3:
        print('가장 큰 수:', num1)
    else:
        print('가장 큰 수:', num3)
else:
    if num2>=num3:
        print('가장 큰 수:', num2)
    else:
        print('가장 큰 수:', num3)



# 최대값을 저장할 변수 도입
max = num1 #첫번째 변수로 시작
if num2 > max:
    max = num2
elif num3 > max:
    max = num3
print('가장 큰수:', max)