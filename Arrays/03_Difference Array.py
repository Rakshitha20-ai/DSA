# Difference Array

numbers = [10, 20, 30, 40, 50]

print("Original array:", numbers)

# Create difference array
difference = [0] * len(numbers)

# Store the first element
difference[0] = numbers[0]

# Calculate differences
for i in range(1, len(numbers)):
    difference[i] = numbers[i] - numbers[i - 1]

print("Difference array:", difference)


# Reconstruct original array
result = [0] * len(numbers)

result[0] = difference[0]

# Add differences to reconstruct values
for i in range(1, len(numbers)):
    result[i] = result[i - 1] + difference[i]

print("Reconstructed array:", result)