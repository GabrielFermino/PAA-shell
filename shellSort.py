import time

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

with open("./Ordenados/o2000000.txt", 'r') as f:
    array = f.readlines()

start = time.time()
shellSort(array)
end = time.time()

print("Valores aleatorios (Shell Sort)")
print("Execution time: ", end - start)