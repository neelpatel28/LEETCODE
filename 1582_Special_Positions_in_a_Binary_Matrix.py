mat1 = [[1,0,0],[0,1,0],[0,0,1]]
mat2 = [[1,0,0],[0,0,1],[1,0,0]]

def Solution(mat):
    count = 0
    rows = len(mat)
    cols = len(mat[0])
    row_sums = [sum(row) for row in mat]
    col_sums = [sum(mat[r][c] for r in range(rows)) for c in range(cols)]
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 1 and row_sums[r] == 1 and col_sums[c] == 1:
                count += 1
    return count

# Logic : We can calculate the sum of each row and column. 
# A position (r, c) is special if mat[r][c] == 1 and the sum of the r-th row and c-th column is 1, 
# which means there is only one '1' in that row and column.
print(Solution(mat1))  # Output: 3
print(Solution(mat2))  # Output: 1