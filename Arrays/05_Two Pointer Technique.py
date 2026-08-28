# Two Pointer Technique

numbers = [10, 20, 30, 40, 50, 60]

target = 70

# Set pointers at both ends
left = 0
right = len(numbers) - 1

# Move pointers until they meet
while left < right:

    # Calculate current pair sum
    current_sum = numbers[left] + numbers[right]

    print(
        "Left:", numbers[left],
        "Right:", numbers[right],
        "Sum:", current_sum
    )

    # Pair found
    if current_sum == target:
        print("Pair found:", numbers[left], numbers[right])
        break

    # Move left pointer to increase the sum
    elif current_sum < target:
        left += 1

    # Move right pointer to decrease the sum
    else:
        right -= 1