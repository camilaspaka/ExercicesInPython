def localizarPorNome(lista):
      busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])

#outro exercicio

def depreciarPorNome(lista, porc):
      depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])

#mais um

def excluirPorSerial(lista):
      serial=int(input("Digite o serial do equipamento que será excluido: "))
  for elemento in lista:
    if elemento[2]==serial:
      lista.remove(elemento)
  return "Itens excluídos."

#ultimo, i promisse <3

def resumirValores(lista):
      valores=[]
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))