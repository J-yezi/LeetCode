'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，
但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。
计算这个岛屿的周长。 

示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16
'''


class Solution(object):
    def islandPerimeter(self, grid):
        relation, total = 0, 0
        for i in range(len(grid)):
            item, count = grid[i], len(grid[i])
            for j in range(count):
                if item[j] == 1:
                    total += 1
                    if j < count - 1 and item[j + 1] == 1:
                        relation += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        relation += 1
        return total * 4 - relation * 2


if __name__ == "__main__":
    s = Solution()
    array = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(s.islandPerimeter(array))
