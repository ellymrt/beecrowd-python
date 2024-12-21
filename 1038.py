cod, quant = input().split(" ")
cod = int(cod)
quant = int(quant)

if cod == 1:
    total = 4*quant
    print("Total: R$ %0.2f"%total)
elif cod == 2:
    total = 4.50*quant
    print("Total: R$ %0.2f"%total)
elif cod == 3:
    total = 5*quant
    print("Total: R$ %0.2f"%total)
elif cod == 4:
    total = 2*quant
    print("Total: R$ %0.2f"%total)
elif cod == 5:
    total = 1.5*quant
    print("Total: R$ %0.2f"%total)