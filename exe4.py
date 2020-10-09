# Exercicio 4

notas = []

for _ in range(4):
    nota = int(input(f'Informe a {_ + 1}º nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'A média das notas é igual á: {media:.1f}')
