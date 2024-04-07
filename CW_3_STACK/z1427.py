n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

saddle_points = 0

for i in range(n):
    min_row = min(matrix[i])
    for j in range(m):
        max_col = max(matrix[row][j] for row in range(n))
        if matrix[i][j] == min_row and matrix[i][j] == max_col:
            saddle_points += 1

print(saddle_points)
