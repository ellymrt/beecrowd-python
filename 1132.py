x = int(input(""))
y = int(input(""))

if y > x:
    a = x
    x = y
    y = a
    
for i in range (x, y+1):
    if i % 13 != 0:
        x = x + i
        
print(x)