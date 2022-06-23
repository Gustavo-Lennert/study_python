print("\t\tEste programa faz a contagem de 1 a 100")
#'\t' = tabulação / espaço em branco

#Criação de variável
numero = int(input("Digite um número: "))

#Inicio do laço de repetição
while numero <= 100:
    print("\t" + str(numero))
    numero = numero + 1
print("Laço encerrado...")