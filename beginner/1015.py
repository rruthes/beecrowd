from math import sqrt 

line1 = input().split()
line2 = input().split()

x1 = float(line1[0])
y1 = float(line1[1])
x2 = float(line2[0])
y2 = float(line2[1])

dif_x = x2 - x1
dif_y = y2 - y1
quad_difx = dif_x * dif_x
quad_dify = dif_y * dif_y
distance = sqrt(quad_difx + quad_dify)
print(f'{distance:.4f}')