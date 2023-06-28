def menu():
    print("Qual operação deseja usar?\n[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[5] Potência")
    opcaoSecundaria = int(input("Opção: "))
    while True:
        if opcaoSecundaria == 1:
            somar()
            break
        elif opcaoSecundaria == 2:
            subtrair()
            break
        elif opcaoSecundaria == 3:
            multiplicar()
            break
        elif opcaoSecundaria == 4:
            dividir()
            break
        elif opcaoSecundaria == 5:
            potencia()
            break
        else:
            print("Opção Inválida", end="")
            opcaoSecundaria = int(input("Digite novamente a opção: "))
    
def somar():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o número a ser somado: "))
    resultado = n1 + n2
    print(f"A soma de {n1} e {n2} é igual a {resultado}.")

def subtrair():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o número a ser subtraído: "))
    resultado = n1 - n2
    print(f"A subtração de {n1} por {n2} é igual a {resultado}.")

def multiplicar():
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite o multiplicador: "))
    resultado = n1 * n2
    print(f"O produto de {n1} e {n2} é igual a {resultado}.")

def dividir():
    n1 = float(input("Digite o numerador: "))
    n2 = float(input("Digite o denominador: "))
    resultado = n1 / n2
    print(f"A divisão de {n1} e {n2} é igual a {resultado}.")

def potencia():
    n1 = float(input("Digite o número: "))
    pot = float(input("Digite o valor da potêcia: "))
    resultado = n1 ** pot
    print(f"{n1} elevado a {pot} é igual a {resultado}")
