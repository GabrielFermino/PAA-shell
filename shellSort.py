import utils

def shellSort(array):
    size = len(array)
    interval = size // 2

    while interval > 0:
        for i in range(interval, size):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

print("Shell Sort:")
print(" ")

print("Valores aleatorios:")
utils.getTime(shellSort, "./Aleatórios/a1000.txt")
print("-----------------")

print("Valores decrescentes:")
utils.getTime(shellSort, "./Decrescentes/d1000.txt")
print("-----------------")

print("Valores crescentes:")
utils.getTime(shellSort, "./Ordenados/o1000.txt")
print("-----------------")

print("Valores parcialmente ordenados:")
utils.getTime(shellSort, "./ParcialmenteOrdenados/po1000.txt")