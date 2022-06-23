print("Este programa faz a análise para atendimentos prioritários")
#Criação de variáveis
nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade: "))

#Estrutura de condição
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")