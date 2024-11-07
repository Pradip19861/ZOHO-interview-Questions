def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        total_sum -= arr[i]
        
        if left_sum == total_sum:
            return i
        
        left_sum += arr[i]
    
    return -1

# Example usage
arr1 = [-7, 1, 5, 2, -4, 3, 0]
arr2 = [1, 2, 3]

print(find_equilibrium_index(arr1))  # Output: 3
print(find_equilibrium_index(arr2))  # Output: -1
