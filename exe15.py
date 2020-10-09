# Exercicio 15

ganho_hora = float(input('Qual o valor recebido por hora de trabalho? '))
horas_trabalhadas = float(input('Quantas horas trabalhadas no mês? '))

ir = 0.11
inss = 0.08
sindicato = 0.05

salario_bruto = ganho_hora * horas_trabalhadas
salario_liquido = salario_bruto - (salario_bruto * ir) - (salario_bruto * inss) - (salario_bruto * sindicato)

print(f'\nSálario Bruto R$ {salario_bruto:.2f}\n'
      f'- IR R${salario_bruto * ir:.2f}\n'
      f'- INSS R${salario_liquido * inss:.2f}\n'
      f'- Sindicato R${salario_bruto * sindicato:.2f}\n'
      f'- Salario Liquido R$ {salario_liquido}')
