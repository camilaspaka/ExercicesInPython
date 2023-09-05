nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa? ").upper()
#primeira parte do problema ser resolvido :3
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para a sala Amarela")
elif doenca_infectocontagiosa=="NÃO":
    print("Encaminhe o paciente para a sala Branca")
else:
    print("Responda a suspeita de doença infecto-contagiosa com SIM ou NÃO")
    #segunda parte do problema :D 
if idade>=65:
    print("Paciente com prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>12:
        gravidez=input("A paciente está gravida? ").upper()
        if gravidez=="SIM":
             print("Paciente com Prioridade")
        else:
            print("Paciente sem prioridade")
    else:
        print("Paciente sem prioridade")