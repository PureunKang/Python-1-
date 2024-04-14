while True: #==while 1: (1 = True) (0=False 라서 안됨)
    num = int(input('숫자를 입력하시오: '))
    if num == -1:
        print('프로그램을 종료합니다.')
        break
    for i in range (num):
        print('*', end='')
    print()
    # if num == -1: 여기에다 종료 넣으면 윗 줄 print() 때문에 '프로그램을 종료합니다'와 인풋 사이에 한 줄 공백 생기니까 그냥 위로 올리기.
    #     print('프로그램을 종료합니다.')
    #     break


