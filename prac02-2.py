money = 120
year = 5
result = money*(1.0+0.06)**year
print('5년 후의 원리금은',money*(1.0+0.06)**5)
print(year, '년 후의 원리금은 ',result, sep='')

money = int(input('투자원금: '))
year = int(input('투자기간: '))
print(year, '년 후의 원리금은 ', money*(1.0+0.06)**year, sep='')
