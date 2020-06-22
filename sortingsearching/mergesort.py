def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end =" ")
    print()

arr = [23,4,5,3,2,76,56,45,34,32,11,23,1,0,98,76]
printList(arr)
MergeSort(arr)
printList(arr)
