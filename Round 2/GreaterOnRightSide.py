# //1.
def replace_with_next_greatest(arr):
    n = len(arr)
    greatest = -1

    for i in range(n-1, -1, -1):
        # Store the current element
        current = arr[i]
        # Replace current element with the greatest element seen so far
        arr[i] = greatest
        # Update the greatest element seen so far
        if current > greatest:
            greatest = current
    
    return arr

# Example usage
arr = [16, 17, 4, 3, 5, 2]
print(replace_with_next_greatest(arr))  # Output: [17, 5, 5, 5, 2, -1]

# // Input:
# // N = 6
# // Arr[] = {16, 17, 4, 3, 5, 2}

# // Output:
# // 17 5 5 5 2 -1
# // Explanation: For 16 the greatest element 
# // on its right is 17. For 17 it's 5. 
# // For 4 it's 5. For 3 it's 5. For 5 it's 2. 
# // For 2 it's -1(no element to its right). 
# // So the answer is 17 5 5 5 2 -1