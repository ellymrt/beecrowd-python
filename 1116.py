N = int(input(""))
for i in range(1, N+1):
    X, Y = map(int, input("").split())
    if Y == 0:
        print("divisao impossivel")
    else:
        print(X / Y)