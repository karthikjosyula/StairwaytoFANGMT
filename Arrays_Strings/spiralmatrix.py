"""
[1,   2,   3]
[4,   5,   6]
[7,   8,   9]
[10, 11,  12]
[13, 14,  15]
[100,101,102]

"""

matrix =[ [1,2,3], [4,5,6], [7,8,9], [10,11,12],[13,14,15], [100,101,102]]
m = len(matrix)
n = len(matrix[0])
rowstart = 0
colstart = 0
rowend = len(matrix)
colend = len(matrix[0])
spiralmat = []
spiralmatcount = 0

while spiralmatcount < m*n:
    if spiralmatcount < m * n:
        for j in range(colstart, colend):
            spiralmat.append(matrix[rowstart][j])
        rowstart+=1
        spiralmatcount = len(spiralmat)
    if spiralmatcount < m * n:
        for i in range(rowstart,rowend):
            spiralmat.append(matrix[i][colend-1])
        colend-=1
        spiralmatcount = len(spiralmat)
    if spiralmatcount < m * n:
        for j in range(colend-1, colstart-1, -1):
            spiralmat.append(matrix[rowend-1][j])
        rowend-=1
        spiralmatcount = len(spiralmat)
    if spiralmatcount < m * n:
        for i in range(rowend-1, rowstart-1, -1):
            spiralmat.append(matrix[i][colstart])
        colstart+=1
        spiralmatcount = len(spiralmat)
print(spiralmat)
