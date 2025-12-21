arr = [5, 4, 3, 2, 1]


def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]
    return arr


print(selectionsort(arr))
