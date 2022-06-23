print("Este programa faz a análise para atendimentos prioritários")
#Criação de variáveis
nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade: "))
#'upper()' = retorna uma cópia da string convertida para maiúscula
doenca_infec = input("Suspeita de doença infectocontagiosa? ").upper()

#Estrutura de condição encadeada
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infec == "SIM":
    print("O paciente " + " deve ser direcionado para a sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")