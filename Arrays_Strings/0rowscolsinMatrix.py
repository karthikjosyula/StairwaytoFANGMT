"""1,1,1
1,0,1
0,1,0
1,2,3
"""
s = [[1,1,1], [1,5,1], [0,1,0], [1,2,3]]

rows, cols = set(), set()
m = len(s)
n = len(s[0])
for i in range(m):
    for j in range(n):
        if s[i][j] == 0:
            rows.add(i)
            cols.add(j)
for i in range(m):
    for j in range(n):
        if i in rows or j in cols:
            s[i][j] = 0

print(s)

