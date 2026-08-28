# Prefix Sum

numbers = [10, 20, 30, 40, 50]

print("Original array:", numbers)

# Create prefix array with initial 0s
prefix = [0] * len(numbers)

print("prefix:", prefix)

# Store the first element
prefix[0] = numbers[0]

# Calculate cumulative sums
for i in range(1, len(numbers)):
    prefix[i] = prefix[i - 1] + numbers[i]

print("Prefix sum:", prefix)


# Find sum from index 1 to 3
left = 1
right = 3

# Calculate range sum
if left == 0:
    range_sum = prefix[right]
else:
    range_sum = prefix[right] - prefix[left - 1]

print("Sum from index 1 to 3:", range_sum)