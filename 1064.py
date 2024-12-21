positivos=0
lista=[]
for i in range (1,7,1):
    num=float(input())
    if num > 0:
        positivos=positivos+1
        lista.append(num)

media=sum(lista) / len(lista)
print(f"{positivos} valores positivos")
print(f"{media:.1f}")