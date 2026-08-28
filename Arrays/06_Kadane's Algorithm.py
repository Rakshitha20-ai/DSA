# Kadane's Algorithm  Find the maximum sum of a contiguous subarray.

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Start with the first element
current_sum = numbers[0]
maximum_sum = numbers[0]

# Check each remaining element
for i in range(1, len(numbers)):

    # Choose between starting a new subarray
    # or adding the current element to the existing subarray
    current_sum = max(numbers[i], current_sum + numbers[i])

    # Update the maximum sum found so far
    maximum_sum = max(maximum_sum, current_sum)

print("Original array:", numbers)
print("Maximum subarray sum:", maximum_sum)