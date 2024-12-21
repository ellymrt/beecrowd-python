from datetime import timedelta

def pegar_data_hora():
    dia = int(input("Dia ").strip())
    hora, minutos, segundos = map(int, input("").split(" : "))
    return timedelta(days=dia, hours=hora, minutes=minutos, seconds=segundos)

inicio = pegar_data_hora()
fim = pegar_data_hora()

tempo = fim - inicio

if tempo.days < 0:
    tempo = timedelta()

dias = tempo.days
horas = tempo.seconds // 3600
minutos = (tempo.seconds % 3600) // 60
segundos = tempo.seconds % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")