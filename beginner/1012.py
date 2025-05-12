line1 = input().split()
a = float(line1[0])
b = float(line1[1])
c = float(line1[2])
pi = 3.14159

triangulo = (a * c) / 2.0
circulo = pi * c * c
trapezio = (a + b) * c / 2.0
quadrado = b * b
retangulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')