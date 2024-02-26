def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    leftArr = arr[:mid]
    rightArr = arr[mid:]

    leftArr = mergeSort(leftArr)
    rightArr = mergeSort(rightArr)

    return merge(leftArr, rightArr)


def merge(leftArr, rightArr):
    arr = []
    leftIdx, rightIdx = 0, 0

    while leftIdx < len(leftArr) and rightIdx < len(rightArr):
        if leftArr[leftIdx] < rightArr[rightIdx]:
            arr.append(leftArr[leftIdx])
            leftIdx += 1
        else:
            arr.append(rightArr[rightIdx])
            rightIdx += 1

    arr.extend(leftArr[leftIdx:])
    arr.extend(rightArr[rightIdx:])

    return arr
