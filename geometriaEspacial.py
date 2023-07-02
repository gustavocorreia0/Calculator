import math

def menu():
    print("""Existem diversos tipos de sólidos geométricos:
          [1] Paralelepipedo
          [2] Prisma regular
          [3] Cone
          [4] Piramide
          [5] Esfera""")
    
    op = int(input('Qual sólido deseja trabalhar: '))
    
    if op == 1:
        Paralelepipedo()
    elif op == 2:
        PrismaRegular()
    elif op == 3:
        Cone()
    elif op == 4:
        Piramide()
    elif op == 5:
        Esfera()
        
        
        
def Paralelepipedo():
    l1 = float(input("Digite o valor da aresta X: "))
    l2 = float(input("Digite o valor da aresta Y: "))
    h = float(input("Digite a altura do paralelepipedo: "))
    
    areaBase = l1*l2
    areaLateral = 2*(l1*h) + 2*(l2*h)
    areaTotal = 2*areaBase + areaLateral
    volume = l1*l2*h
    
    print(f"Medidas do Paralelepipedo:\nÁrea da base: {areaBase}\nÁrea lateral: {areaLateral}\nÁrea Total: {areaTotal}\nVolume: {volume}")
    
    
def PrismaRegular():
    lado = float(input("Digite o tamanho da aresta: "))
    h = float(input("Digite a altura: "))
    
    while True:
        qnt = int(input("Quantos lados possuem o prisma: "))
        
        if qnt < 3:
            print("Um polígono deve ter pelo menos 3 lados.")
        
        if qnt == 3:
            areaBase = (lado ** 2 * math.sqrt(3)) / 4
            break
        
        if qnt == 4:
            areaBase = lado ** 2
            break
        
        if qnt == 5:
            cotangente = 1 / math.tan(math.pi / 5)
            areaBase = (5/4) * lado ** 2 * cotangente
            break
        
        if qnt == 6:
            areaBase = (3 * math.sqrt(3) * lado ** 2) / 2
            break
        
        if qnt >= 7:
            print("O limite de lados suportados é 6.")
    
    areaLateral = qnt * h * lado
    areaTotal = areaLateral + 2*areaBase
    volume = areaBase * h
    
    print(f"Medidas do Prisma:\nÁrea da base: {areaBase}\nÁrea lateral: {areaLateral}\nÁrea Total: {areaTotal}\nVolume: {volume}")
    
    
def Cone():
    r = float(input("Digite o raio da base: "))
    h = float(input("Digite a altura do cone: "))
    
    areaBase = (math.pi * r ** 2) / 2
    areaLateral = (math.sqrt(r**2 + h**2))**2 * math.pi / 2
    areaTotal = areaBase + areaLateral
    volume = areaBase * h / 3 
    
    print(f"Medidas do Cone:\nÁrea da base: {areaBase}\nÁrea lateral: {areaLateral}\nÁrea Total: {areaTotal}\nVolume: {volume}")
    
    
def Piramide():
    l = float(input("Digite o valor do lado da pirâmide: "))
    h = float(input("Digite a altura do cone: "))
    
    areaBase = l**2
    areaLateral = (l/2 * h)*4 
    areaTotal = areaBase + areaLateral
    volume = areaBase * h / 3 
    
    print(f"Medidas do Piramide:\nÁrea da base: {areaBase}\nÁrea lateral: {areaLateral}\nÁrea Total: {areaTotal}\nVolume: {volume}")
    
    
def Esfera():
    r = float(input("Digite o raio da esfera: "))
 
    areaTotal = 4 * math.pi * r ** 2
    volume =  4/3 * math.pi * r ** 3
    
    print(f"Medidas do Piramide:\nÁrea Total: {areaTotal}\nVolume: {volume}")
    