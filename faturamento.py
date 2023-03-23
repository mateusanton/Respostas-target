import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

menorValor = float('inf')
maiorValor = float('-inf')
somaValores = 0
numDias = 0

for dia in dados:
    valor = dia['valor']
    if valor > maiorValor:
        maiorValor = valor
    if valor < menorValor:
        menorValor = valor
    if valor > 0:
        somaValores += valor
        numDias += 1


mediaMensal = somaValores / numDias

numDiasAcimaDaMedia = 0

for dia in dados:
    valor = dia['valor']
    if valor > mediaMensal:
        numDiasAcimaDaMedia += 1

print(f"Menor valor de faturamento diário: R$ {menorValor:.2f}")
print(f"Maior valor de faturamento diário: R$ {maiorValor:.2f}")
print(f"Número de dias com faturamento acima da media: {numDiasAcimaDaMedia}")
