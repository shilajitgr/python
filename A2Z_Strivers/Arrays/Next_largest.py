def next_greater_element(arr):
    n = len(arr)
    next_greater = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            next_greater[index] = arr[i]
        stack.append(i)

    return next_greater

# Example usage
arr = [4, 5, 2, 25, 7, 8, 6]
result = next_greater_element(arr)
print("Array:", arr)
print("Next Greater Elements:", result)
