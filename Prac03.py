k = []
sum = 0
# 1 <= num <= 100
for i in range (1,101):
    if i%3==0 and i%2!=0:
        k.append(i)
        sum += i
print(k)
print('평균:', sum/len(k))


