# Exercicio 17
import math

area = float(input('tamanho em metros quadrados:'))

litro = area/6
latas18 = (area)/(108)
galao = (area)/(21.6)

if area > 0:
    preco = math.ceil(latas18)*80
    print(f'A quantidade de latas de 18 litros a serem compradas é: {math.ceil(latas18)}\n'
          f'Preço total é de: {preco} reais')
    preco2 = math.ceil(galao)*25
    print(f'A quantidade de galao de 3.6 litros a serem compradas é {math.ceil(galao)}\n'
          f'Preço total foi: {preco} reais')
else:
    print('Dados invalidos')