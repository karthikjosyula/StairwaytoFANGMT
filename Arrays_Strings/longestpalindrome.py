"""
s = "cbcdcbedcbc"
plen = 0
indexhash = []
indexhash.append(0)
indexhash.append(1)
def isvalidpalindrome(s):
    tlen = 0
    k = 0
    l = len(s)
    while k <= l:
        if s[k] != s[l-1]:
            break
        k+=1
        l-=1
    if k > l:
        tlen = len(s)
    return tlen

for i in range(len(s)):
    for j in range(len(s)-1, i, -1):
        if s[i] == s[j] and len(s[i:j+1]) > plen:
            tmp = isvalidpalindrome(s[i:j+1])
            if tmp > plen:
                plen = tmp
                indexhash[0] = i
                indexhash[1] = j+1
print(s[indexhash[0]: indexhash[1]])
"""
#s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s = "aaaaaa"
plen = 0
indexhash = []
indexhash.append(0)
indexhash.append(1)
i = 0
j = len(s)
def isvalidpalindrome(s):
    tlen = 0
    k = 0
    l = len(s)
    while k <= l:
        if s[k] != s[l-1]:
            break
        k+=1
        l-=1
    if k > l:
        tlen = len(s)
    return tlen

while i < len(s)-1:
    if len(s[i:j]) <= plen:
        break
    else:
        while j > i:
            if len(s[i:j]) <= plen:
                break
            elif s[i] == s[j-1]:
                tmp = isvalidpalindrome(s[i:j])
                if tmp > plen:
                    plen = tmp
                    indexhash[0] = i
                    indexhash[1] = j
            j-=1
    j = len(s)
    i+=1
print(s[indexhash[0]: indexhash[1]])







