line = input().split()
code = int(line[0])
qtt = int(line[1])

if code == 1:
    value = 4.0
elif code == 2:
    value = 4.5
elif code == 3:
    value = 5.0
elif code == 4:
    value = 2.0
elif code == 5:
    value = 1.5

final_v = value * qtt
print(f'Total: R$ {final_v:.2f}')