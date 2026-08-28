# Sliding Window

numbers = [10, 20, 30, 40, 50, 60]

k = 3

# Calculate the first window sum
window_sum = sum(numbers[:k])
maximum = window_sum

print("Initial window sum:", window_sum)

# Slide the window through the array
for i in range(k, len(numbers)):
    window_sum = window_sum + numbers[i] - numbers[i - k]

    print("Current window sum:", window_sum)

    # Update maximum sum
    maximum = max(maximum, window_sum)

print("Maximum sum of", k, "consecutive elements:", maximum)