idade = int(input())

anos = idade // 365
resto_dias = idade % 365

meses = resto_dias // 30
dias = resto_dias % 30

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')