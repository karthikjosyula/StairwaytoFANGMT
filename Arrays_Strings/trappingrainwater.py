#Trapped rain water

s = [0,0,1,0,0,3,0,2,1,0]
vol = 0
max_l = 0
max_r = 0
l = 0
r = len(s)-1
while l < r:
    if s[l] < s[r]:
        if max_l <= s[l]:
            max_l = s[l]
            l+=1
        else:
            vol+= (max_l - s[l])
            l+=1

    else:
        if max_r <= s[r]:
            max_r = s[r]
            r-=1
        else:
            vol+= (max_r - s[r])
            r-=1
print(vol)
