import statistics

def menu():
    print("Opções:\n[1] Média\n[2] Moda\n[3] Mediana")
    while True:
        opcaoSecundaria = int(input("Opção: "))
    
        if opcaoSecundaria == 1:
            Media()
            break
        elif opcaoSecundaria == 2:
            Moda()
            break
        elif opcaoSecundaria == 3:
            Mediana()
            break
        else:
            print("Opção Inválida!")

# Média
def Media():
    numeros = []
    qnt = int(input("Quantos termos deseja adicionar: "))

    for x in range(qnt):
        n = float(input(f"Digite o número de ordem {x}: "))
        numeros.append(n)
    
    media = statistics.mean(numeros)
    
    print("Valores digitados:")
    for x in range(len(numeros)):
        print(numeros[x], end="\t")
    
    print(f"\nMédia dos valores inseridos: {media}")

# Moda
def Moda():
    numeros = []
    qnt = int(input("Quantos termos deseja adicionar: "))
    
    for x in range(qnt):
        n = int(input(f"Digite o número de ordem {x}: "))
        numeros.append(n)
    
    moda = statistics.mode(numeros)

    print("Números digitados:")
    for n in numeros:
        print(n,end=" ")
    
    print(f"A moda da lista de números é {moda}")


# Mediana
def Mediana():
    numeros = []
    qnt = int(input("Quantos termos deseja adicionar: "))

    for x in range(qnt):
        n = int(input(f"Digite o número de ordem {x}: "))
        numeros.append(n)
    
    mediana = statistics.median(numeros)

    print("Números digitados:")
    for n in numeros:
        print(n,end=" ")

    print(f"A mediana da lista de números é {mediana}")