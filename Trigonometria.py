import math

def menu():
    print("""Qual operação deseja usar?
[1] Seno
[2] Cosseno
[3] Tangente""")
    while True:
        opcaoSecundaria = int(input("Opção: "))
    
        if opcaoSecundaria == 1:
            seno()
            break
        elif opcaoSecundaria == 2:
            cosseno()
            break
        elif opcaoSecundaria == 3:
            tangente()
            break
        else:
            print("Opção Inválida!")

def seno():
    a = int(input("Digite o ângulo: "))
    resultado = math.sin(math.radians(a))
    print(f"O seno do ângulo {a}º é igual a {resultado}")

# Cosseno
def cosseno():
    a = int(input("Digite o ângulo: "))
    resultado = math.cos(math.radians(a))
    print(f"O cosseno do ângulo {a}º é igual a {resultado}")

# Tangente
def tangente():
    a = int(input("Digite o ângulo: "))
    resultado = math.tan(math.radians(a))
    print(f"A tangente do ângulo {a}º é igual a {resultado}")
