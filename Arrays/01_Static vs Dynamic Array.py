# Static vs Dynamic Array

numbers = [10, 20, 30, 40]
    
print("Original array:", numbers)

# Accessing elements
print("First element:", numbers[0])
print("Third element:", numbers[2])

# Updating an element
numbers[1] = 200

print("After updating:", numbers)

# Adding an element
numbers.append(50)

print("After adding 50:", numbers)

# Removing last element
numbers.pop()

print("After removing last element:", numbers)

# Adding multiple elements
numbers.extend([60, 70])

print("After adding multiple elements:", numbers)
