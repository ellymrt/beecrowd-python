dentro = 0
fora = 0
numeros = []

n = int(input())
while n >= 10000:
    n = int(input())
        
for i in range(0, n):
    num = int(input())
    numeros.append(num)
    
for nub in numeros:
    if nub >= 10 and nub <=20:
        dentro += 1
    else:
        fora += 1
        
print(f"{dentro} in")
print(f"{fora} out")