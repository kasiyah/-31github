# def rotate(matrix):
#     # TODO
#     matrix1 = []
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i,n):
#             matrix1[i][j] = matrix[(n-j-1)][i]
#     return matrix1

def rotate(matrix):
    n = len(matrix)
 
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row

    return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(rotate(matrix))
#Output: [[7,4,1],[8,5,2],[9,6,3]]


"""
Explanation:

n = len(matrix) 
- Get the number of rows/columns in the square matrix and store it in the variable n.

Transpose the matrix: 
a. for i in range(n): 
- Start a loop that iterates over the rows. 
b. for j in range(i, n): 
- Start a nested loop that iterates over the columns starting from the current row i. 
- This ensures we only swap elements in the upper triangle of the matrix, avoiding double swaps. 
c. matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 
- Swap the elements at positions (i, j) and (j, i).

Reverse each row: 
a. for row in matrix: 
- Start a loop that iterates over each row in the matrix. 
b. row.reverse() 
- Reverse the elements in the current row.

The time complexity of this code is O(n^2), as both the transpose and reverse steps involve nested loops 
that iterate over all the elements in the matrix. The space complexity is O(1), as the rotation is performed 
in-place without allocating any additional data structures.

"""