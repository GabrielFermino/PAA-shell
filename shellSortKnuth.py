import time

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

with open("./Aleatórios/a500000.txt", 'r') as f:
    array = f.readlines()

start = time.time()
shellSortWithKnuth(array)
end = time.time()

print("Valores aleatorios (Shell Sort)")
print("Execution time: ", end - start)