def insert_sort(unsort_array):
    n = len(unsort_array)

    for i in range(1, n):
        unsort_value = unsort_array[i]
        j = i - 1
        while j >= 0:
            if unsort_value < unsort_array[j]:
                unsort_array[j+1] = unsort_array[j]
                j -= 1
            else:
                break
        unsort_array[j+1] = unsort_value 
        

    sort_array = unsort_array
    return sort_array
                    
unorder = [4, 5, 6, 3, 2, 1]
order = insert_sort(unorder)
print(order)
