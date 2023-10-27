depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])