def bubble_sort(unsort_array):
    n = len(unsort_array)

    for i in range(n):
        check_swap = False
        for j in range(n-i-1):
            if unsort_array[j] > unsort_array[j+1]:
                unsort_array[j], unsort_array[j+1] = unsort_array[j+1], unsort_array[j]
                check_swap = True
        if not check_swap:
            break
    sort_array = unsort_array
    return sort_array

unorder = [4, 5, 6, 3, 2, 1]
order = bubble_sort(unorder)
print(order)
