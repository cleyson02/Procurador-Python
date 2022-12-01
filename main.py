lista = [50, 1, 30, 40, 9, 8, 10]
num = int(input("Digite o número que deseja procurar: "))

def procurar(lista,num):
    for i in range(len(lista)):
        if(lista[i] == num):
            return True

    return False

print(procurar(lista,num))