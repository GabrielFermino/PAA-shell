import time

def checkArrayIsSorted(array):
    size = len(array)
    for i in range(1, size):
        if array[i] < array[i - 1]:
            return False
    return True

def openFile(filename):
    with open(filename, 'r') as f:
        array = [int(x) for x in f.read().split()]
    return array

def getTime(func, filename):
    array = openFile(filename)
    start = time.time()
    func(array)
    end = time.time()
    print("O vetor esta ordenado? ", checkArrayIsSorted(array))
    print("Tempo de execucao: ", end - start)