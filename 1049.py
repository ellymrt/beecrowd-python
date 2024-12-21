tipo1 = str(input(""))
tipo2 = str(input(""))
tipo3 = str(input(""))

if tipo1 == "vertebrado":
    if tipo2 == "ave":
        if tipo3 == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if tipo3 == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if tipo2 == "inseto":
        if tipo3 == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if tipo3 == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")