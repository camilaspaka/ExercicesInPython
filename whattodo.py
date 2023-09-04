nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65:
    print("O paciente " + nome + " possui atendimento prioritário!")
elif doenca_infectocontagiosa=="Sim":
    print("O paciente " + nome + " deve ser direcionado a sala de espera reservada.")
else:
    print("O paciente " + nome + " não possui atendimento prioritário e pode aguardar")