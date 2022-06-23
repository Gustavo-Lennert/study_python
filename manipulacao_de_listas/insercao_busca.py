#parte 3 manipulação de listas

print("\nEste programa faz a execução de lista mútiplas(índices) para cadastro e consulta de dados")

#Criação da variável que vai armazenar a lista, que poderá receber várias entradas de diversos tipos
# [] = representa um receptor de uma lista
aluno = []
idade = []
curso = []
mensal = []

#Criação de váriavel
cadAluno = "S"
consult = "C"
cont=0

#Estrutura de condição while (enquanto a variável "reposta" for igual a "S", repita a execução)
while cadAluno=="S":
    print("\nInsira as informações do aluno")

    # "append" - inserir/acrescentar o valor a lista
    # "\" (contra barra) - possibilita a apresentação de caracter como texto
    aluno.append(input("Nome do aluno: "))
    idade.append(int(input("Idade: ")))
    curso.append(input("Curso: "))
    mensal.append(float(input("Mensalidade: ")))
    cadAluno=input("Digite \"S\" para continuar: ").upper()

while consult == "C":
    busca= input("\nInsira o nome do aluno que gostaria de consultar: ")

    #Estrutura de repetição para apresentar os valores inseridos na lista
    # "indice" - representa um contador que irá ler cada campo das listas inseridas, e apresentar conforme foi solicitado
    # "in range(0,len(aluno))" - condição que determina que será atribuido ao "indice" o valor de 0 até a quantidade de 
    # elementos existentes na lista "aluno", para que possa apresentá-los   
    for indice in range(0,len(aluno)):

        #Estrutura de condição para comparar o valor da variável "busca" com cada valor cadastrado na lista, se for encontrado irá executar a apresentação dos dados
        if(busca == aluno[indice]):
            print("\n" + "Aluno: " + aluno[indice] + " / " + "RGM - ", (indice+1))
            print("Idade: ", idade[indice])
            print("Curso matriculado: ", curso[indice])
            print("Mensalidade: R$", mensal[indice]) 

    consult=input("\nDigite \"C\" para continuar: ").upper()