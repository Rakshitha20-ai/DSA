# Matrix Transpose

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Get number of rows and columns
rows = len(matrix)
columns = len(matrix[0])

# Create an empty list for transpose
transpose = []

# Loop through each column
for j in range(columns):

    row = []

    # Take elements from each row of the current column
    for i in range(rows):
        row.append(matrix[i][j])

    # Add the new row to transpose
    transpose.append(row)


# Print original matrix
print("Original matrix:")

for row in matrix:
    print(row)


# Print transposed matrix
print("Transpose:")

for row in transpose:
    print(row)