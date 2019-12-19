def solution(obstacleGrid):
    x = len(obstacleGrid)
    y = len(obstacleGrid[0])
    if(obstacleGrid[0][0]==1):return 0
    
    for i in range(x):
        for j in range(y):
            if i == 0 and j == 0:
                obstacleGrid[i][j] = 1
            elif i == 0 :
                obstacleGrid[i][j] = int(obstacleGrid[i][j]==0 and obstacleGrid[i][j-1]==1)
            elif j == 0:
                obstacleGrid[i][j] = int(obstacleGrid[i][j]==0 and obstacleGrid[i-1][j]==1)
            else:
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        print(obstacleGrid)
    return obstacleGrid[x-1][y-1]
            
print(solution([[0,0,0],[0,1,0],[0,0,0]]))
