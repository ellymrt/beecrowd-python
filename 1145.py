X, Y = map(int, input("").split())
if 1 < X < 20 and X < Y < 100000:
    for i in range(1, Y + 1):
        if i % X == 0:
            print(i) 
        else:
            print(i, end=" ")
