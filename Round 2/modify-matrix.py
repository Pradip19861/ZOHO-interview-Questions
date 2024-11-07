def modify_matrix(mat):
    M = len(mat)
    N = len(mat[0])
    new_mat = [row[:] for row in mat]
    
    # Iterate through each cell in the original matrix
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1:
                # Set adjacent cells to 0
                if i > 0:           # Top cell
                    new_mat[i - 1][j] = 0
                if i < M - 1:       # Bottom cell
                    new_mat[i + 1][j] = 0
                if j > 0:           # Left cell
                    new_mat[i][j - 1] = 0
                if j < N - 1:       # Right cell
                    new_mat[i][j + 1] = 0
    
    return new_mat

# Example usage
mat = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
]

modified_mat = modify_matrix(mat)
for row in modified_mat:
    print(row)

# Output:
# [0, 0, 0]
# [0, 0, 0]
# [1, 0, 1]
