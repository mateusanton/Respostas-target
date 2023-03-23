# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

valores = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

valorTotal = sum(valores.values())
print(f"Valor total: R${valorTotal}")

percentuais = {estado: (valor /valorTotal)*100 for estado, valor in valores.items()}
for estado, percentual in percentuais.items():
  print(f"{estado}: {percentual:.2f}%")

