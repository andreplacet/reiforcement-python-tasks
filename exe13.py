# Exercicio 13

sexo = str(input('Informe seu Sexo [M/F]: ')).lower()
altura = float(input('Informe sua Altura: '))

formula = (72.7 * altura) - 58

if sexo[0] == 'f':
    formula = (62.7 * altura) - 44.7

print(f'Seu peso ideal é. {formula}')