import math
import basico, Trigonometria, geometriaPlana, estatistica


print("Bem-vindo(a) à Calculadora Científica!")

print("A Calculadora possui algumas áreas, dentre elas:")
print("""[1] Aritmética Básica
[2] Trigonometria
[3] Geometria Plana
[4] Estatística""")
while True:

    op = int(input("Qual área da matemática deseja usar?\nOpção: "))

    if op == 1:
        basico.menu()
    elif op == 2:
        Trigonometria.menu()
    elif op == 3:
        geometriaPlana.menu()
    elif op == 4:
        estatistica.menu()
    else:
        print("Opção Inválida")
        continue

    off = input("Deseja usar a calculadora novamente? ").lower()

    if off == "s" or off == "sim":
        print("""[1] Aritmética Básica
[2] Trigonometria
[3] Geometria Plana
[4] Estatística""")
    else:
        print("Obrigado e volte sempre!")
        break




