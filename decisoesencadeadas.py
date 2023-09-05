nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
if idade>=65:
    print("Paciente com Prioridade")
    if doenca_infectocontagiosa=="SIM":
       print("Encaminhe o paciente para a sala Amarela")
    elif doenca_infectocontagiosa=="NÃO":
       print("Encaminhe o paciente para a sala Branca")
else:
   print("O paciente não tem prioridade")
   if doenca_infectocontagiosa=="SIM":
      print("Encaminhe o paciente para a sala Amarela")   
   elif doenca_infectocontagiosa=="NÃO":
      print("Encaminhe o paciente para a sala Branca") 
   else:
      print("Responda a suspeita de doença infectocontagiosa com SIM ou NÂO.")     