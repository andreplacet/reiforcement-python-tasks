# Exericio 11
from math import pow

num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe o segundo número inteiro: '))
num3 = float(input('Informe um número real: '))

a = (num1 * 2) + (num2 / 2)
b = (num1 * 3) + (num3 * 3)
c = pow(num3, 3)

print(f'O produto do dobro do primeiro com metade do segundo {a:.2f}')
print(f'A soma do triplo do primeiro com terceiro {b:.2f}')
print(f'O Terceiro elevado ao cubo {c:.2f}')
