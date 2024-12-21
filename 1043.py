a, b, c = map(float, input().split())

if (a + b > c) and (b + c > a) and (c + a > b):
    perimetro = a+b+c
    print("Perimetro = %0.1f"%perimetro)
else:
    area = ((a+b)*c)/2
    print("Area = %0.1f"%area)