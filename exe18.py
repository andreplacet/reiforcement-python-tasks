# Excercicio 18

tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (Mbps): '))

formula = tamanho / (velocidade / 60)

print(f'Tempo aproximado de download em minutos : {formula:.0f}')
