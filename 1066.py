pares=0
impares=0
positivos=0
negativos=0
for i in range (1,6,1):
    num=float(input())
    if num % 2 == 0:
        pares=pares+1
    else:
        impares=impares+1
    
    if num < 0:
        negativos=negativos+1
    elif num > 0:
        positivos=positivos+1
        
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")