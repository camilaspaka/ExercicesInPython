nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
    #não sei porque mas o elif não ta funcionando...chateação 
    #descobri o porque, resolvido ja
    #código será alterado para preencher todas as possibilidades
if idade>=65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para a Sala Amarela - Com Prioridade")
elif idade <65 and doenca_infectocontagiosa=="SIM":
    print("O paciente será direcionado para a Sala Amarela - Sem Prioridade")
elif idade>=65 and doenca_infectocontagiosa=="NÃO":
    print("O paciente será direcionado para a Sala Branca - Com prioridade")
else:
    print("Responda a suspeita da doença infectocontagiosa com SIM ou NÃO")