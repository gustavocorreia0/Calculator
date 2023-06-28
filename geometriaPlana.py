import math

def menu():
    print("""Qual figura deseja trabalhar?
[1] Quadrado
[2] Retângulo
[3] Triângulo
[4] Círculo""")
    opcaoSecundaria = int(input("Opção: "))
    while True:
        if opcaoSecundaria == 1:
            Quadrado()
            break
        elif opcaoSecundaria == 2:
            Retangulo()
            break
        elif opcaoSecundaria == 3:
            Triangulo()
            break
        elif opcaoSecundaria == 4:
            Circulo()


def Quadrado():
    l = float(input("Digite o lado do quadrado: "))

    opcaoTerciaria = input("Deseja calcular área ou perímetro? [A/P]\t").lower()

    if opcaoTerciaria == "a" or opcaoTerciaria == "area" or opcaoTerciaria == "área":
        print(f"A área do quadrado é {l*l}")
    elif opcaoTerciaria == "p" or opcaoTerciaria == "perimetro" or opcaoTerciaria == "perímetro":
        print(f"O perimetro do quadrado é {4*l}")


def Retangulo():
    b = float(input("Digite a base do retângulo: "))
    h = float(input("Digite a altura do retângulo: "))

    opcaoTerciaria = input("Deseja calcular a área ou perímetro? [A/P]\t").lower()

    if opcaoTerciaria == "a" or opcaoTerciaria == "area" or opcaoTerciaria == "área":
        print(f"A área do retângulo é {b*h}")
    elif opcaoTerciaria == "p" or opcaoTerciaria == "perimetro" or opcaoTerciaria == "perímetro":
        print(f"O perímetro do retângulo é {2*b + 2*h}")



def Triangulo():
    print("Qual é o tipo de triângulo que vamos trabalhar?\n[1] Equilátero\n[2] Isósceles\n[3] Escaleno")
    tipo = int(input("Opção: "))
    
    if tipo == 1:
       
        l = float(input("Digite a medida dos lados: "))

        area = l**2*math.sqrt(3)/4
        perimetro = 3*l
    
        while True:

            op = input("Deseja calcular área ou perímetro? [A/P] ").lower()

            if op == "a" or op == "area" or op == "área":

                print(f"A área do triângulo é igual a {area}")
                break

            elif op == "p" or op == "perimetro" or op == "perímetro":

                print(f"O perímetro do triângulo é igual a {perimetro}")
                break

            else:

                print("Comando inválido.")

    elif tipo == 2:

        base = float(input("Digite a base do triângulo (lado único): "))
        l = float(input("Digite agora os lados que possuem a mesma medida: "))

        semip = (l + l + base) / 2
        perimetro = 2*l + base
        area = math.sqrt(semip * (semip - l) * (semip - l) * (semip - base))

        while True:

            op = input("Deseja calcular área ou perímetro? [A/P] ").lower()

            if op == "a" or op == "area" or op == "área":

                print(f"A área do triângulo é igual a {area}")
                break

            elif op == "p" or op == "perimetro" or op == "perímetro":

                print(f"O perímetro do triângulo é igual a {perimetro}")
                break

            else:

                print("Comando inválido.")
                
        
    elif tipo == 3:

        l1 = float(input("Digite a medida do lado 1: "))
        l2 = float(input("Digite a medida do lado 2: ")) 
        l3 = float(input("Digite a medida do lado 3: "))

        semip = (l1 + l2 + l3) / 2
        area = math.sqrt(semip * (semip - l1) * (semip - l2) * (semip - l3))

        while True:

            op = input("Deseja calcular área ou perímetro? [A/P] ").lower()

            if op == "a" or op == "area" or op == "área":

                print(f"A área do triângulo é igual a {area}")
                break

            elif op == "p" or op == "perimetro" or op == "perímetro":

                print(f"O perímetro do triângulo é igual a {perimetro}")
                break

            else:

                print("Comando inválido.")


def Circulo():
    raio = float(input("Digite o valor do raio: "))

    area = raio**2*math.pi
    perimetro = 2*math.pi*raio

    while True:
        op = input("Deseja calcular área ou perímetro? [A/P] ").lower()
        if op == "a" or op == "area" or op == "área":
            print(f"A área do círculo é igual a {area}")
            break
        elif op == "p" or op == "perimetro" or op == "perímetro":
            print(f"O perímetro do círculo é igual a {perimetro}")
            break
        else:
            print("Comando inválido.")
