busca=input("
Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamento)):
    if busca==equipamento[indice]:
       print("Valor...: ", valores[indice])
       print("Serial: ", seriais[indice])