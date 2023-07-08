def mergesort(array: list):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left: list, right: list):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list

array_1 = [19, 2, 1, 0, 4, 5, 6, 9, 10]

print(mergesort(array_1))
