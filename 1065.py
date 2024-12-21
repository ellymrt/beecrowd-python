pares=0
for i in range (1,6,1):
    num=float(input())
    if num % 2 == 0:
        pares=pares+1

print(f"{pares} valores pares")