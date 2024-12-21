a, b = map(int, input().split())

if a < b:
    horas = b-a
else:
    horas = b+24-a
print("O JOGO DUROU {} HORA(S)".format(horas))