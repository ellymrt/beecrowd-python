nota1 = float(input(""))
while nota1 < 0 or nota1 > 10:
    print("nota invalida")
    nota1 = float(input(""))
    pass
    
nota2 = float(input(""))
while nota2 < 0 or nota2 > 10:
    print("nota invalida")
    nota2 = float(input(""))
    pass

soma = nota2 + nota1
media = soma / 2

print(f"media = {media}")