equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.apped(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite "S" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.....: ", equipamentos[indice])
    print("Valor.......: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento: ", departamentos[indice])
    
        