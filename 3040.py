N = int(input())

for i in range(1, N+1):
    h, d, g = map(int, input().split(" "))
    if (h >= 200 and h <= 300) and (d >= 50) and (g >= 150):
        print("Sim")
    else:
        print("Não")