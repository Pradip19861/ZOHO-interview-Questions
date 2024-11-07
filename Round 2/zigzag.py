def zigzag_traversal(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # There will be rows + cols - 1 diagonals
    for diag in range(rows + cols - 1):
        # Determine the starting point
        if diag < rows:
            row = diag
            col = 0
        else:
            row = rows - 1
            col = diag - rows + 1
        
        # Collect the diagonal elements
        diagonal = []
        while row >= 0 and col < cols:
            diagonal.append(matrix[row][col])
            row -= 1
            col += 1
        
        # If the diagonal number is even, reverse the order to follow the zig-zag pattern
        if diag % 2 == 0:
            result.extend(diagonal)
        else:
            result.extend(diagonal[::-1])
    
    return result

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(zigzag_traversal(matrix))  # Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
