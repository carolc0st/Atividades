
def calcularOperacao(operador):
    num1 = 0
    num2 = 0
    if operador == 1:
       print("Digite o primeiro número: ")
       num1 = int(input())
       print("Digite o segundo número: ")
       num2 = int(input())
       return ("O valor da soma: " + str(num1 + num2))
    elif operador == 2:    
       print("Digite o primeiro número: ")
       num1 = int(input())
       print("Digite o segundo número: ")
       num2 = int(input())
       return("O valor da subtração "+ str(num1 - num2))
    elif operador == 3:
       print("Digite o primeiro número: ")
       num1 = int(input())
       print("Digite o segundo número: ")
       num2 = int(input())
       return("O valor da multiplicação: " + str(num1 * num2))
    elif operador == 4:
       print("Digite o primeiro número: ")
       num1 = int(input())
       print("Digite o segundo número: ")
       num2 = int(input())
       return("O valo da divisão: "+ str(num1 / num2))
    elif operador == 0:
       return("Calculadora encerrada ")
    else:
       return "Essa opção não existe"

operacao = 1
while operacao != 0:
    print("\nEscolha uma opção")
    print("1-Soma")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    print("0-Sair")
    operacao = int(input())

    resultado = calcularOperacao(operacao)
    print(resultado)


    





    


