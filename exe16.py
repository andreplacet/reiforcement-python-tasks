# Exercicio 16

area = float(input('Tamanho em metros quadrados: '))
litros = area / 3

if area % 54 == 0:
    latas = area / 54
else:
    latas = int(area / 54) + 1

preco = latas * 80
print(f'{latas} latas')
print(f'R$ {preco:.2f}')
