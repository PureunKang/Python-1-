num = int(input('자연수 입력: '))
for i in range (1, num+1):
    if num%i==0:
        print(i, end=' ')

#과정
# if ??:
#   print(i, end=' ')
# 이렇게 작성해 놓고, ?? 범위 어떻게 정할지 생각해 본다.
# 나머지없이 딱 떨어지면 약수라고 하니까 그거 생각해서 범위지정!
