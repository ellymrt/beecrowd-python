positivos=0

for i in range (1,7,1):
    num=float(input())
    if num > 0:
        positivos = positivos + 1

print(f"{positivos} valores positivos")