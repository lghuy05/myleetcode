arr = [5, 4, 3, 2, 1]


def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left = mergesort(left_half)
    right = mergesort(right_half)

    return merged(left, right)


def merged(left_half, right_half):
    i = j = 0
    merged_arr = []
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1

    while i < len(left_half):
        merged_arr.append(left_half[i])
        i += 1
    while j < len(right_half):
        merged_arr.append(right_half[j])

    return merged_arr


print(mergesort(arr))
