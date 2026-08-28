# Right Array Rotation

numbers = [10, 20, 30, 40, 50]

k = 2

# Keep k within the array length
k = k % len(numbers)

# Move the last k elements to the front
rotated = numbers[-k:] + numbers[:-k]

print("Original array:", numbers)
print("After right rotation:", rotated)

# Left Array Rotation

numbers = [10, 20, 30, 40, 50]

k = 2

rotated = numbers[k:] + numbers[:k]

print("Original array:", numbers)
print("After left rotation:", rotated)