import random

def quick_begin(unsort_array):
    low, high = 0, len(unsort_array)-1
    quick_sort(unsort_array, low, high)
    return unsort_array 

def quick_sort(A, low, high):
    if low < high:
        random_pivot = random.randint(low, high)
        A[random_pivot], A[high] = A[high], A[random_pivot]

        pivot = partition(A, low, high)
        quick_sort(A, low, pivot-1)
        quick_sort(A, pivot+1, high)

def partition(A, low, high):
    i, pivot = low, high

    for j in range(low, high):
        if A[j] < A[pivot]:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[i], A[pivot] = A[pivot], A[i]
    return i

unorder = [5, 3, 8, 6, 2, 7, 1, 4]
order = quick_begin(unorder)
print(order)
