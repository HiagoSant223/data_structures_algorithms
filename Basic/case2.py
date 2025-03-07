#Automvel faz 12km por litro
# Obter tempo gasto na viagem
# Velocidade média durante a viagem

# Distancia percorida = Tempo * Velocidade

# Com a distancia calcular a QTD Litros gasto com a formula - Litros_gasto = Distancia / 12

# Apresentar: 
# valor velocidade media
# Tempo gasto na viagem
# Distancia percorrida na viagem
# Quantidade de Litros

tempo_gasto = float(input('Digite quantas horas levou a viagem: '))
velocidade_media = float(input('Digite qual foi a velocidade media do percurso: '))

distancia = tempo_gasto * velocidade_media

litros_gastos = distancia / 12

print(f'A velocidade media do percurso foi: ', velocidade_media)
print(f'Tempo total da viagem: ', tempo_gasto)
print(f'Distancia percorrida: ', distancia)
print(f'Quantidade de litros utilizado na viagem: ', round(litros_gastos,2))