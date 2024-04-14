k = []
'''
3
29
38
12
57
74
48
85
61
'''
for i in range (9):
    num = int(input())
    k.append(num)
# 1. 반복문
max = 0
max_inx = -1
for i in range(9):
    if k[i] > max:
        max = k[i]
        max_idx = i
print(max)
print(max_idx+1)

# 2. 파이썬 함수 사용
print(max[k])
print(k.index(max(k))+1)
