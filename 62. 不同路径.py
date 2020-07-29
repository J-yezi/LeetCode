# coding=utf-8

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
"""


class Solution(object):
    """
    递归
    利用回溯加剪枝，但是会超时
    """
    def uniquePaths1(self, m, n):
        ans = []

        def recursion(array, m, n):
            if not m and not n:
                ans.append(array[:])
                return
            if m:
                array.append("向右")
                recursion(array, m - 1, n)
                array.pop()
            if n:
                array.append("向下")
                recursion(array, m, n - 1)
                array.pop()
        recursion([], m - 1, n - 1)
        return len(ans)

    """
    动态规划
    我们令 dp[i][j] 是到达 i, j 最多路径
    动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]

    生成的原始数组是[[1, 1], [1, 0], [1, 0]]
    1表示到达这个位置只有一种可能，也就是最开始动态规划的原始解
    因为是只能向下或者向右，所以第一列都是1，因为就只有一种可能
    """
    def uniquePaths2(self, m, n):
        dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
        print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    ans = s.uniquePaths2(3, 2)
    print(ans)
