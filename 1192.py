N = int(input())

for i in range(1, N+1):
    sequencia = input("")
    a = int(sequencia[0])  
    b = sequencia[1] 
    c = int(sequencia[2])
    
    if a == c:
        numero = a * c
    elif b.islower():
        numero = a + c
    elif b.isupper():
        numero = c - a
    print(numero)