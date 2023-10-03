inventario={}
opcao=int(input("Digite: "
            "<1> para registrar ativo"
            "<2> para persistir em arquivo"
            "<3> para exibir ativos armazenados: "))
while opcao>0 and opcao<4:
    if opcao==1:
        resp="S"
        while resp=="S":
            inventario[input("Digite o número patrimonial: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
            resp=input("Digite <S> para continuar.").upper()
    elif opcao==2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + 
					valor[1] + ";" +valor[2]+"")
                print("Persistido com sucesso!")
    elif opcao==3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines())
    opcao=int(input("Digite: "
            "<1> para registrar ativo"
            "<2> para persistir em arquivo"
            "<3> para exibir ativos armazenados: "))
    
#parte do exercico  

    from Funcoes.Funcoes_Arquivos import *
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        print(exibir())
    opcao = chamarMenu()

    #outra parte, posso alterar a qualquer momento

    from Funcoes.Funcoes_Arquivos import *
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
        for linha in resultado:
            print(linha[2:-1])
    opcao = chamarMenu()

    #testar depois 

    from Funcoes.Funcoes_Arquivos import *
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        resultado = exibir()
        for linha in resultado:
            print(linha[linha.find(";")+1:-1])
    opcao = chamarMenu()

    #solução de tudo acima

    for linha in resultado:
        separacao=linha[linha.find(";")+1:-1]
        data=separacao[0:separacao.find(";")]
        separacao = separacao[separacao.find(";")+1:-1]
        descricao=separacao[0:separacao.find(";")]
        departamento=linha[linha.rfind(";")+1:-1]
        print("Data.........: ", data)
        print("Descrição....: ", descricao)
        print("Departamento.: ", departamento)
opcao = chamarMenu()

#exercicio

for linha in resultado:
        lista=linha.split(";")
        print("Data.........: ", lista[1])
        print("Descrição....: ", lista[2])
        print("Departamento.: ", lista[3])
opcao = chamarMenu()