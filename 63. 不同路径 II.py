# coding=utf-8

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""


class Solution(object):
    """
    动态规划
    和上一道题差不多，只是生成数组的时候，全部生成0
    如果是第一个位置那么就为1
    如果是靠边上的内置，就直接等于上一个位置的值
    如果是碰到阻挡，那么当前位置就为0
    如果不靠边的，那么就使用动态规划来计算
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if not i and not j:
                        dp[i][j] = 1
                    elif not i:
                        dp[i][j] = dp[i][j - 1]
                    elif not j:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__":
    dp = [[0]]
    s = Solution()
    print(s.uniquePathsWithObstacles(dp))
