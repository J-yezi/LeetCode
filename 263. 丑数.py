"""
编写一个程序判断给定的数是否为丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:
输入: 6
输出: true
解释: 6 = 2 × 3
"""


class Solution(object):
    def isUgly(self, num):
        while num:
            if num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            else:
                return True if num == 1 else False
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(0))
