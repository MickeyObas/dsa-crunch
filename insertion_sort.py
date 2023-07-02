# A simple insertion sort implementation 

def insertion_sort_1(array: list):
    # Non-decreasing order
    for j in range(1, len(array)):
        i = j - 1
        key = array[j]
        while i > -1 and array[i] > key:
            array[i + 1] =  array[i]
            i -= 1
        array[i+1] = key
    return array

test_array = [4, 2, 1, 19, 11, 0]

print(insertion_sort_1(test_array))

def insertion_sort_2(array: list):
    # Non-increasing order
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1
        array[i+1] = key
    return array

print(insertion_sort_2(test_array))
    

