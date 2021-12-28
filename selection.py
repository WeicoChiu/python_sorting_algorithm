def selection_sort(unsort_array):
    n = len(unsort_array)

    for i in range(0, n):
        min_value = unsort_array[i]
        for j in range(i, n):
            if min_value > unsort_array[j]:
                min_value, unsort_array[j] = unsort_array[j], min_value
        min_value, unsort_array[i] = unsort_array[i], min_value
    
    sort_array = unsort_array
    return sort_array
            
unorder = [4, 5, 6, 3, 2, 1]
order = selection_sort(unorder)
print(order)
