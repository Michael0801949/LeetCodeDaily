# Q1 62. Unique Paths: https://leetcode.com/problems/unique-paths/
# dp(recurrence)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. meaning of dp array: dp array is a 2 dimention matrix, each number means the number of unique path to that location
        dp = [[0] * m for _ in range(n)]
        # 3. initialize dp array: location on the top row and left column need to be initialized as 1 becasue they are required to get the other path and there is only one unique path to them
        for x in range(0, m):
            dp[0][x] = 1
        for y in range(0, n):
            dp[y][0] = 1
        # 4. iteration order: top left to bottom right
        for i in range(1, n):
            for j in range(1, m):
                # 2. recurrence formula: the # of unique path to location i, j is sum the # of unique path to the top and left location
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]

# recurssive
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    
# Q2 63. Unique Paths II: https://leetcode.com/problems/unique-paths-ii/
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        # 1. meaning of dp array: same as Q1
        dp = [[0] * m for _ in range(n)]
        # 3. initialize dp array
        # diff vs Q1, initialization need to make 0 as 1 until there is obstacle
        for x in range(0, m):
            if obstacleGrid[0][x] == 0:
                dp[0][x] = 1
            else:
                break
        for y in range(0, n):
            if obstacleGrid[y][0] == 0:
                dp[y][0] = 1
            else:
                break
        # 4. iteration order: top left to bottom right
        for i in range(1, n):
            for j in range(1, m):
                    # diff from Q1, need to skip when iterate to the obsitacle location
                    if obstacleGrid[i][j] == 1:
                        continue
                    # 2. recurrence formula:same as Q1
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]