'''
Q)  주어진 딕셔너리 데이터를 다음처럼 출력해 보시오.
    Tip) for문과 f포맷팅 문자열 이용

    ↓ 실행화면 ↓
    <성인 입장료 - 8000원>
    <청소년 입장료 - 5000원>
    <어린이 입장료 - 3000원>
'''
ticket = {'성인': 8000, '청소년': 5000, '어린이': 3000}

# for i in ticket:
#     print('f<{i} 입장료 - {value}원)

for key in ticket:
    print(f'<{key} 입장료 - {ticket[key]}원>')