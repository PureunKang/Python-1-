numA = int(input('정수를 입력하시오: ')) #일단 나누기로 진행해보고 그 다음 연산진행방향 정하기.
a = numA//100
b = (numA/10)%10
c = numA%10
print('백의 자리수는 ', a)
print('십의 자리수는 ', b)
print('일의 자리수는 ', c)