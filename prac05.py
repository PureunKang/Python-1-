while True:
    print()
    a = float(input('짐의 무게는 얼마입니까? '))
    if a==0:
        print('프로그램 종료')
        break
    if a>=10: #elif a>=10 <<<이걸로 표현해야 됨...
        print('수수료는 10,000원 입니다.')
    if 0< a <10: #else: <<이걸로 표현해야 됨..
        print('수수료는 없습니다.')
