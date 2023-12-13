def rotate(matrix):
    # TODO
    matrix1 = []
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix1[i][j] = matrix[(n-j-1)][i]
    return matrix1

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate(matrix))
#Output: [[7,4,1],[8,5,2],[9,6,3]]