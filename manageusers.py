usuarios={}
opcao=input("O que deseja realizar?" +
            "<I> - Para Inserir um usuário"+
            "<P> - Para Pesquisar um usuário"+
            "<E> - Para Excluir um usuário"+
            "<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
chave=input("Digite o login: ").upper()
usuarios[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                 input("Digite a última data de acesso: "),
                 input("Qual a última estação acessada: ").upper()]
    opcao = input("O que deseja realizar?" +
                  "<I> - Para Inserir um usuário" +
                  "<P> - Para Pesquisar um usuário" +
                  "<E> - Para Excluir um usuário" +
                  "<L> - Para Listar um usuário: ").upper()

from dicionario import *
usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()