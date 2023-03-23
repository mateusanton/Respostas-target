texto = input("Digite o que quer inverter: ")

textoInvetido = ""

for i in range(len(texto)-1, -1, -1):
    textoInvetido += texto[i]

print(textoInvetido)