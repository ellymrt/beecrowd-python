cod1, peca1, valor1 = input().split(" ")
cod1 = int(cod1)
peca1 = int(peca1)
valor1 = float(valor1)

cod2, peca2, valor2 = input().split(" ")
cod2 = int(cod2)
peca2 = int(peca2)
valor2 = float(valor2)

total1 = peca1 * valor1
total2 = peca2 * valor2

total = total1 + total2

print("VALOR A PAGAR: R$ %0.2f"%total)