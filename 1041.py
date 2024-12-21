x, y=map(float, input().split())

if (y > 0) and (x > 0):
    print("Q1")
elif(x==0):
    print("Eixo X")
elif(y==0):
    print("Eixo Y")
elif (y > 0) and (x < 0):
    print("Q2")
elif (y < 0) and (x < 0):
    print("Q3")
elif (y < 0) and (x > 0):
    print("Q4")
elif (y==x==0):
    print("Origem") 