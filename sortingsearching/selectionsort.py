s = [10,1,40,2,160,30,2,30,0]
i = 0
#j = 0
#minindex = 0
l = len(s)
if l<2:
    print(None if l == 0 else s[1])
else:
    while i < l-1:
        minindex = i
        j = i+1
        while j < l:
            if s[j] < s[minindex]:
                minindex = j
            j+=1
        s[i], s[minindex] = s[minindex], s[i]
        i+=1
    print(s)
