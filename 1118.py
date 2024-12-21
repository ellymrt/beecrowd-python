while True:
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

    print(f"media = {media:.2f}")
    print("novo calculo (1-sim 2-nao)")
    msg = int(input(""))
    while msg != 1 and msg != 2:
        print("novo calculo (1-sim 2-nao)")
        msg = int(input(""))
         
    if msg == 2:
        break
    else:
        True
    