line1 = input().split()
a = int(line1[0])
b = int(line1[1])
c = int(line1[2])
amb = a - b
if amb < 0:
    maior_ab = (a + b - amb)  / 2
else:
    maior_ab = (a + b + amb) / 2

if maior_ab > c:
    print(f'{maior_ab:.0f} eh o maior')
else:
    print(f'{c:.0f} eh o maior')