# Bubble Sort

from ..randomArray import getRandomArray

#arr = [1, 3, 2]
arr = getRandomArray(10)

isSorted = False

print(arr)

while not isSorted:
    isSorted = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            isSorted = False

print(arr)