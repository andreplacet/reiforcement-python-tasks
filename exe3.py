# Exercicio 3

lista = []

for _ in range(2):
    num = int(input(f'{_ + 1}º - Informe um número: '))
    lista.append(num)

print(f'A soma dos valores digitados é igual á: {sum(lista)}')
