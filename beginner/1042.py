line = list(map(int, input().split()))
maior = max(line)
menor = min(line)

for item in line:
    if item != maior and item != menor:
        meio = item
        break

print(menor)
print(meio)
print(maior)
print("")
print(line[0])
print(line[1])
print(line[2])