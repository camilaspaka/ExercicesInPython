equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamentos: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite "S" para continuar: ").upper()

for equipamento in equipamentos:
    print("Equipamento: ", equipamento)    