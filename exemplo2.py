print("Digite números para adicionar a lista (digite 'done' para terminar): ")
numeros = []
while True:
    entrada = input()
    if entrada.lower() == 'done':
        break
    else:
        numeros.append(int(entrada))
print("Números coletados: ", numeros)
