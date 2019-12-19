def solution(grid):
    x = len(grid)
    y = len(grid[0])
    for i in range(x):
        for j in range(y):
            if i == 0 and j == 0:grid[i][j] = grid[i][j]
            elif i == 0 :grid[i][j] = grid[i][j] + grid[i][j-1]
            elif j == 0:grid[i][j] = grid[i][j] + grid[i-1][j]
            else:grid[i][j] = grid[i][j] + min(grid[i-1][j],grid[i][j-1])
        print(grid)
    return grid[x-1][y-1]
            
print(solution([[1,3,1],[1,5,1],[4,2,1]]))
