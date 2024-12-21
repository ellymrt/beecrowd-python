from datetime import timedelta

horaInicio, minInicio, horaFim, minFim = map(int, input().split())

comeco = timedelta(hours=horaInicio, minutes=minInicio)
final = timedelta(hours=horaFim, minutes=minFim)

if comeco == final:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    if final < comeco:
        final += timedelta(days=1)

    duracao = final - comeco

    horas = duracao.seconds // 3600
    minutos = (duracao.seconds // 60) % 60

    print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")