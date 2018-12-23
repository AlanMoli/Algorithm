def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        low = [i for i in array[1:] if i < pivot]
        high = [i for i in array[1:] if i > pivot]
        return quick_sort(low) + [pivot] + quick_sort(high)


print(quick_sort([1, 9, 3, 7, 5]))
