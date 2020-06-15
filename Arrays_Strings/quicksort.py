def myquicksort(input):
    return quick_sort(input, 0, len(input)-1)
#Quick Sort
def quick_sort(A, l, h):
    #if h-l < 25 and l<h:
    #    selectionsort(A)
    if l<h:
        p = partition(A, l, h)
        quick_sort(A,l,p-1)
        quick_sort(A,p+1,h)
    return A

def get_pivot(A, l, h):
    mid = (l+h)//2
    pivot = h
    if (A[l] < A[mid] and A[mid] < A[h]) or (A[l] > A[mid] and A[mid] > A[h]):
        pivot = mid
    elif (A[mid] < A[l] and A[l] < A[h]) or (A[mid] > A[l] and A[l] > A[h]):
        pivot = l
    return pivot

def partition(A, l ,h):
    pivotIndex = get_pivot(A, l, h)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[l] = A[l], A[pivotIndex]
    border = l

    for i in range(l,h+1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[l], A[border] = A[border], A[l]
    return border
#Selection Sort
def selectionsort(A):
    l = len(A)
    for i in range(0,l-1):
        minindex = i
        for j in range(i+1,l):
            if A[j] < A[minindex]:
                minindex = j
        if minindex != i:
            A[i], A[minindex] = A[minindex], A[i]
    return A

print(myquicksort([0,41,51,61,71,81,12,34,25,27,34,35,36,39,62,91,21,99,33,11,87,3,4,5,6,1,7,282]))
