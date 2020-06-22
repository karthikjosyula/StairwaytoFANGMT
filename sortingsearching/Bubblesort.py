s = [8,22,7,5,1,34,56,11,73,14,3,6]
l = len(s)
for i in range(0,l-1):
    for j in range(0, l-1-i):
        if s[j] > s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(s)