import sys

def merge_begin(unsort_array):
    low, high = 0, len(unsort_array)-1
    merge_sort(unsort_array, low, high)
    return unsort_array

def merge_sort(A, low, high):
    if low < high:
        mid = low + (high - low) // 2
        merge_sort(A, low, mid)
        merge_sort(A, mid+1, high)
        merge(A, low, mid, high)

def merge(A, low, mid, high):
    leftsub, rightsub = A[low: mid+1], A[mid+1: high+1]
    leftindex, rightindex = 0, 0
    leftsub.append(sys.maxsize)
    rightsub.append(sys.maxsize)
   
    for i in range(low, high+1):
        if leftsub[leftindex] <= rightsub[rightindex]:
            A[i] = leftsub[leftindex]
            leftindex += 1
        else:
            A[i] = rightsub[rightindex]
            rightindex += 1
    
unorder = [5, 3, 8, 6, 2, 7, 1, 4]
order = merge_begin(unorder)
print(order)
