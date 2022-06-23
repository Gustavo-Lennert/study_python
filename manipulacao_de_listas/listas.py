#parte 1 manipulação de listas

print("\nEste programa faz a execução de lista simples de produtos")

#Criação da variável que vai armazenar a lista, que poderá receber várias entradas de diversos tipos
# [] = representa um receptor de uma lista
inventario=[]

#Criação de váriavel
resposta="S"
cont=0

#Estrutura de condição while (enquanto a variável "reposta" for igual a "S", repita a execução)
while resposta=="S":

    print("\nInsira as informações sobre o produto")
    # "append" - inserir/acrescentar o valor a lista
    # "\" (contra barra) - possibilita a apresentação de caracter como texto
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta=input("Digite \"S\" para continuar: ").upper()

#Estrutura de repetição para apresentar os valores inseridos na lista
# "elemento" - variável para receber os valores da lista "inventario" e apresentá-los   
for elemento in inventario:
   print("\n" + " - " + str(elemento))