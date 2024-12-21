valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

for cedulas in cedulas:
    qtd_cedulas = int(valor / cedulas)
    print("{} nota(s) de R$ {},00".format(qtd_cedulas, cedulas))
    valor -= qtd_cedulas*cedulas