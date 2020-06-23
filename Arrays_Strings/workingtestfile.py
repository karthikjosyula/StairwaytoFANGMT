#selection sort
s = [1,32,43,65,76,3,2,45,89,90,87,5,3,4,6,23,45]
l = len(s)
i = 0
while i < (l-1):
    mi = i
    j = i+1
    while j < l:
        if s[j] < s[mi]:
            mi = j
        j+=1
    s[i], s[mi] = s[mi], s[i]
    i+=1
print("Selection sort for s:")
print(s)
i = 0
j = 0
l = 0
#Bubble sort
s1 = [1,32,43,65,76,3,2,45,89,90,87,5,3,4,6,23,45]
l = len(s1)
for i in range(l):
    for j in range(l - 1 - i):
        if s1[j] > s1[j+1]:
            s1[j], s1[j+1] = s1[j+1], s1[j]

print("Bubble  sort for s1:")
print(s1)
l = 0
i = 0
j = 0
#Insertion Sort
s2 = [1,32,43,65,76,3,2,45,89,90,87,5,3,4,6,23,45]
l = len(s2)
for k in range(1,l):
    temp = s2[k]
    for j in range(k):
        if s2[j] > temp:
            s2[j], temp = temp, s2[j]
    s2[k] = temp


print("insertion  sort for s1:")
print(s2)