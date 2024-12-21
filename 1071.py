lista=[]

x=int(input())
y=int(input())

if x > y:
    x, y = y, x

for i in range(x+1,y):
    if i % 2 != 0:
        lista.append(i)

print(sum(lista))