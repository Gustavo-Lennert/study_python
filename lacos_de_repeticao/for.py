print("Este programa simula uma tabuada de um número")

#Criação de variável
tabuada = int(input("Digite um número para exibir a tabuada: "))
print ("Tabuada do número ", tabuada)

#Inicio do laço de repetição
#'in range' = durante os limites / '1,11,1' = valor de inicio| valor de limite / incremento 
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))
