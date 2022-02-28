import utils

def shellSortWithKnuth(array):
    size = len(array)
    interval = 1

    while interval < size / 3:
        interval = interval * 3 + 1

    while interval > 0:
        for i in range(interval, size):
            temp = array[i]
            j = i

            while j > interval - 1 and array[j - interval] >= temp:
                array[j] = array[j - interval]
                j = j - interval

            array[j] = temp
        interval = (interval-1)//3

print("Shell Sort Knuth:")
print(" ")

print("Valores aleatorios:")
utils.getTime(shellSortWithKnuth, "./Aleatórios/a1000.txt")
print("-----------------")

print("Valores decrescentes:")
utils.getTime(shellSortWithKnuth, "./Decrescentes/d1000.txt")
print("-----------------")

print("Valores crescentes:")
utils.getTime(shellSortWithKnuth, "./Ordenados/o1000.txt")
print("-----------------")

print("Valores parcialmente ordenados:")
utils.getTime(shellSortWithKnuth, "./ParcialmenteOrdenados/po1000.txt")