nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
if idade>=65:
    print("O paciente " + nome + " possui atendimento prioritário!")
elif doenca_infectocontagiosa=="SIM":
    print("O paciente " + nome + " deve ser direcionado a sala de espera reservada.")
else:
    print("O paciente " + nome + " não possui atendimento prioritário e pode aguardar")

    #não sei porque mas o elif não ta funcionando...chateação 
    #descobri o porque, resolvido ja