# 2D Array / Matrix Traversal

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix row by row
print("Matrix:")

for row in matrix:
    print(row)


# Print all elements using row and column indexes
print("\nAll elements:")

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")

    print()


