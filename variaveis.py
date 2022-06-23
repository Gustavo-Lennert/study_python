print("Este programa faz apresentação de conteúdos armazenados em váriaveis")

#Criação de váriaveis
nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtd_func = int(input("Digite a quantidade de funcionarios: "))
mediaMensal = float(input("Digite a média da mensalidade: "))

#Apresentação do conteúdo das váriaveis
# '+' e ',' = concatenação / 'str' = transforma o conteúdo em texto(string)
print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtd_func, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensal))

print("-----------Verificação do tipo de dados-----------")
print("O tipo da variável [nome] é: ", type(nome))
print("O tipo da variável [empresa] é: ", type(empresa))
print("O tipo da variável [qtd_func] é: ", type(qtd_func))
print("O tipo da variável [mediaMensal] é: ", type(mediaMensal))