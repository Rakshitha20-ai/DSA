# Row Sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate the sum of each row
for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print("Row", i + 1, "sum:", row_sum)


# Column Sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Go through each column
for j in range(len(matrix[0])):

    column_sum = 0

    # Go through each row for the current column
    for i in range(len(matrix)):
        column_sum += matrix[i][j]

    print("Column", j + 1, "sum:", column_sum)