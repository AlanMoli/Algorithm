def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def bubble_sort(array):
    j = len(array) - 1
    while j > 0:
        i = 0
        while i < j:
            if array[i] > array[i+1]:
                swap(array, i, i+1)
            i += 1
        j -= 1
    return array


print(bubble_sort([1, 9, 3, 7, 5]))
