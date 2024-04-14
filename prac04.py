sign = input('신호등의 색깔 입력(R, G, Y):',)
#if sign == 'R' or 'r' #if sign =='R' or True 로 인식해서 아무값 넣어도 다 정지! 나옴
if sign == 'R' or sign== 'r':
    print('정지!')
if sign == 'G' or sign =='g':
    print('진행~')
if sign == 'y' or sign== 'Y':
    print('주의')