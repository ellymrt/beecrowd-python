conjunto = []

while True:
    m, n = map(int, input().split(" "))
    soma=0
    if (m > 0) and (n > 0):
        conjunto.append(m)
        conjunto.append(n)
        conjunto.sort()
        soma=sum(range(conjunto))
    else:
        break

    print(f"{conjunto} Sum={soma}")