def tran_matrix(mat):
    row1 = len(mat)
    col1 = len(mat[0])
    tran = [[0 for _ in range(row1)] for _ in range(col1)]
    for i in range(row1):
        for j in range(col1):
            tran[j][i] = mat[i][j]
    return tran

matrix = [[1,2,3],
          [4,5,6]]

trans = tran_matrix(matrix)

for row in trans :
    print(row)