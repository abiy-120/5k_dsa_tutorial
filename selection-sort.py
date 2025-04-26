def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                arr[j] = arr[i]
                arr[i] = min
    return arr

selectionSort([8,1,2,2,3])