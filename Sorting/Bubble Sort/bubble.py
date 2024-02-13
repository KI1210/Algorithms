# Bubble Sort

arr = [1, 3, 2]

isSorted = False

while not isSorted:
    isSorted = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            isSorted = False

print(arr)