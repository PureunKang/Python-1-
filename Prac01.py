#q1
a = ['Banana', 'Apple', 'Orange']
a.append('Tomato')
print(a)
del a[1] #또는 a.remove('Apple')
print(a)

#q2
b = (-10, 0, 10,20,30,40,50)
print(b[2:6])
print(len(b))

#q3
ticket = {'성인': 8000, '청소년': 5000, ' 아동': 5000}
print(ticket)

c={}
c['성인']=8000
c['청소년']=8000
c['아동']=8000
print(c)

del c['아동']
print(c)
c['어린이']= 3000
print(c)