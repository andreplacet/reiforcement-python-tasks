# Exercicio 14

peso = float(input('Informe o peso: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00
    print(f'O peso excedeu o valor permitido de 50kg, a multa residual é de '
          f'R$4.00 por kilo excedente\nO peso informado foi de {peso}Kgs e a '
          f'multa total pelo excedido é de R${multa:.2f} reais')
else:
    print(f'O peso não excedeu o limite de 50kg, portanto não gerou multa!')
