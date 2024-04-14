age = int(input('나이를 입력하세요:'))
height = int(input('키를 입력하세요:'))
if age>=40:
    if height>=175:
        print('키가 큽니다')
    else:
        print('키가 보통입니다.')
# if age<40:
#     if height>=180:
#         print('키가 큽니다')
#     else:
#         print('키가 보통입니다')

else:
    if cm>=180:
        print('키가큽니다.')
    else:
        print('키가 보통입니다.')


#논리연산자
if (age>=40 and height>=175) or (age<40 and height>=180):
    print('키가 큽니다.')
else:
    print('키가 보통입니다')