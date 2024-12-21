N = int(input())
final = []
numeros = []

for i in range(0, N, 1):
    nub = input()
    numeros = list(map(float, nub.split()))
    soma = numeros[0] * 2 + numeros[1] * 3 + numeros[2] * 5
    media = soma / (2 + 3 + 5)
    final.append(media)
        
for i in final:
    print(f"{i:.1f}")