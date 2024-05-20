
def calculoIdade(anoNascimento):
    try:
        ano = int(anoNascimento)
        if(ano > 1922) and (ano < 2021):
            anoAtual = 2022
            return anoAtual - ano
        else: 
            print("Digite o ano entre 1922 e 2021")
            return 0
    except:
        print("Digite um valor válido")
        return 0

resultado = 0

print("Digite seu nome completo: ")
nome = str(input())
while resultado == 0:
    print("Digite seu ano de nascimento que seja entre 1922 e 2021: ")
    anoNascimento = input()
    resultado = calculoIdade(anoNascimento)
    if resultado != 0:
        print("Nome: " + nome + "\n Idade: " + str(resultado) + " anos")
       