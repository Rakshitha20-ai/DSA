# Rotate Matrix 90 Degrees Clockwise

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")

for row in matrix:
    print(row)


# Step 1: Transpose the matrix
# Swap elements across the main diagonal
for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# Step 2: Reverse each row
# This completes the 90-degree clockwise rotation
for row in matrix:
    row.reverse()


print("After 90 degree clockwise rotation:")

for row in matrix:
    print(row)