line = list(map(float, input().split()))
A, B, C = map(float, input().split())

if (A + B > C) and (A + C > B) and (B + C > A):
    perimeter = A + B + C
    print("Perimetro = {:.1f}".format(perimeter))
else:
    area = ((A + B) * C) / 2
    print("Area = {:.1f}".format(area))