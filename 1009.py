nomeVendedor = input()
salFixo = float(input())
vendasEmDinheiro = float(input())

comissao = (vendasEmDinheiro * 15)/100
salFinal = salFixo + comissao

print("TOTAL = R$ %0.2f"%salFinal)