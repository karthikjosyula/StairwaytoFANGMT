"""Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]"""
matrix =[  [1,2,3],  [4,5,6],  [7,8,9] ]
n = len(matrix[0])
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
    matrix[i].reverse()
print(matrix)
