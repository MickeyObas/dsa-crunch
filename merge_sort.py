def mergesort(array: list):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    mergesort(left)
    mergesort(right)

    return merge(left, right, array)


def merge(left: list, right: list, array: list):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    return array

array_1 = [19, 2, 1, 0, 4, 5, 6, 9, 10]

print(mergesort(array_1))
