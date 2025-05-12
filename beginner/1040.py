line = input().split()
n1 = float(line[0])
n2 = float(line[1])
n3 = float(line[2])
n4 = float(line[3])

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10.0
print(f'Media: {media:.1f}')

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 == media or media <= 6.9:
    print("Aluno em exame.")
    n_exame = float(input())
    print(f'Nota do exame: {n_exame:.1f}')
    nova_media = (n_exame + media) / 2
    if nova_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f'Media final: {nova_media:.1f}') 