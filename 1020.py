idadeDias = int(input())

ano = idadeDias // 365
idadeDias %= 365
meses = idadeDias // 30
idadeDias %= 30

print(f"{ano:.0f} ano(s)")
print(f"{meses:.0f} mes(es)")
print(f"{idadeDias:.0f} dia(s)")