s = [4,1,56,43,23,76,8,7,2,3,4,11,34,21]
l = len(s)

for k in range(1, l):
    temp = s[k]
    for i in range(k):
        if temp < s[i]:
            temp, s[i] = s[i], temp
    s[k] = temp
print(s)

s[:5] = 0
print(s)