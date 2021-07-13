arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo!")

arquivo.close()

with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\n HakunaMatata!!")

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

    with open("primeiro_arquivo.txt", "r") as arquivo:
        conteudo = arquivo.readline()
        for linha in arquivo.readlines():
           print(linha)