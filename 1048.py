salarioInicial = float(input())

if salarioInicial >= 0 and salarioInicial <= 400.00:
    novoSalario = ((salarioInicial/100)*15)+salarioInicial
    reajuste = salarioInicial/100*15
    print("Novo salario: %0.2f"%novoSalario)
    print("Reajuste ganho: %0.2f"%reajuste)
    print("Em percentual: 15 %")
elif salarioInicial >= 400.01 and salarioInicial <= 800.00:
    novoSalario = ((salarioInicial/100)*12)+salarioInicial
    reajuste = salarioInicial/100*12
    print("Novo salario: %0.2f"%novoSalario)
    print("Reajuste ganho: %0.2f"%reajuste)
    print("Em percentual: 12 %")
elif salarioInicial >= 800.01 and salarioInicial <= 1200.00:
    novoSalario = ((salarioInicial/100)*10)+salarioInicial
    reajuste = salarioInicial/100*10
    print("Novo salario: %0.2f"%novoSalario)
    print("Reajuste ganho: %0.2f"%reajuste)
    print("Em percentual: 10 %")
elif salarioInicial >= 1200.01 and salarioInicial <= 2000.00:
    novoSalario = ((salarioInicial/100)*7)+salarioInicial
    reajuste = salarioInicial/100*7
    print("Novo salario: %0.2f"%novoSalario)
    print("Reajuste ganho: %0.2f"%reajuste)
    print("Em percentual: 7 %")
else:
    novoSalario = ((salarioInicial/100)*4)+salarioInicial
    reajuste = salarioInicial/100*4
    print("Novo salario: %0.2f"%novoSalario)
    print("Reajuste ganho: %0.2f"%reajuste)
    print("Em percentual: 4 %")