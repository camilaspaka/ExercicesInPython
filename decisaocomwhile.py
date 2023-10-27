resposta="SIM"
while resposta=="SIM":
    nivel=input("Digite o nível de acesso: ").upper()
    if nivel=="ADM" or nivel=="USR":
        genero=input("Digite o seu genero: ").upper
        if nivel=="ADM":
            if genero=="FEMININO":
                print("Olá administradora")
            else:
                print("Olá administrador")
        else:
            if genero=="FEMININO":
                print("Olá usuaria")
            else:
                print("Olá usuario")
    elif nivel=="GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta=input("Diite SIM para continuar: ").upper()        