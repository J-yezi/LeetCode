'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

进阶：
你能不使用循环或者递归来完成本题吗？
'''


class Solution:
    # 暴力法
    # def isPowerOfThree(self, n):
    #     i = 1
    #     while i < n:
    #         i *= 3 
    #     return i == n

    # 1162261467是整数范围内最大的幂指
    # def isPowerOfThree(self, n):
    #     return 1162261467 % n == 0 and n > 0

    # 递归
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            if n % 3 == 0:
                return self.isPowerOfThree(n / 3)
            else:
                return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(12))
