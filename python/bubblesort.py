arr = [5, 4, 3, 2, 1]


def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


print(bubblesort(arr))
