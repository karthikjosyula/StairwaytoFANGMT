#Selection Sort
def selectionsort(A):
    l = len(A)
    for i in range(0,l):
        minindex = i
        for j in range(i+1,l):
            if A[j] < A[minindex]:
                minindex = j
        if minindex != i:
            A[i], A[minindex] = A[minindex], A[i]
    return A

print(selectionsort([12,6,42,32,65,12,7,6,5,4,23,56,8,9]))
