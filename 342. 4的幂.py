'''
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:
输入: 16
输出: true
'''


class Solution:
    # 暴力法
    # def isPowerOfFour(self, num):
    #     i = 1
    #     while i < num:
    #         i *= 4
    #     return i == num

    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        if (num & num - 1) != 0:
            return False
        # 1010101010101010101010101010101 最大的4的幂数，也等于0x55555555
        # 如果与运算之后是本身则是 4 的幂
        if (num & 0x55555555) != num:
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfFour(16))
