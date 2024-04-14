price = int(input('입력: '))
if price < 5000:
    print('할인받는금액: 0')
elif price >=5000 and price <10000 :
    print('할인받는금액:', int(price*0.05))
elif price >=10000 and price>5000 :
    print('할인받는금액:', int(price*0.1))
elif price >=50000 and price>10000 :
    print('할인받는금액:', int(price*0.2))

#답안 -> 코드를 효율적으로 짜야한다!
price = int(input('입력: '))
rate = 0 #할인율

if price>=50000:
    rate = 0.2
elif price >=10000:
    rate = 0.1
elif price >=5000:
    rate = 0.05
else:
    rate = 0

print('할인받는금액:', int(price*rate))

