def flood_fill(screen, x, y, newColor):
    M = len(screen)
    N = len(screen[0])
    originalColor = screen[x][y]
    
    # If the original color is the same as the new color, no need to do anything
    if originalColor == newColor:
        return screen
    
    # Define directions for adjacent cells (top, bottom, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def dfs(x, y):
        # Check bounds and if the current cell is of the original color
        if x < 0 or x >= M or y < 0 or y >= N or screen[x][y] != originalColor:
            return
        # Set the new color
        screen[x][y] = newColor
        # Perform DFS on all adjacent cells
        for dx, dy in directions:
            dfs(x + dx, y + dy)
    
    # Start the flood fill from the given coordinates
    dfs(x, y)
    
    return screen

# Example usage
screen = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],
    [1, 2, 2, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],
    [1, 1, 1, 1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1, 2, 2, 1]
]
x, y, newColor = 4, 4, 3

modified_screen = flood_fill(screen, x, y, newColor)
for row in modified_screen:
    print(row)

# Output:
# [1, 1, 1, 1, 1, 1, 1, 1]
# [1, 1, 1, 1, 1, 1, 0, 0]
# [1, 0, 0, 1, 1, 0, 1, 1]
# [1, 3, 3, 3, 3, 0, 1, 0]
# [1, 1, 1, 3, 3, 0, 1, 0]
# [1, 1, 1, 3, 3, 3, 3, 0]
# [1, 1, 1, 1, 1, 3, 1, 1]
# [1, 1, 1, 1, 1, 3, 3, 1]
