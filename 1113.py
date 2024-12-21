def decrescente_crescente (X, Y):
    if X > Y: print("Decrescente")
    else: print("Crescente")
    
while True:
    X, Y = map(int, input().split())
    if X == Y:
        break
    decrescente_crescente(X, Y)