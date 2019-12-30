#coding=utf-8

'''
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt，完全平方数保证了平方后也是整数
'''

class Solution:
    # 暴力法
    # def isPerfectSquare(self, num):
    #     i = 1
    #     while i * i < num:
    #         i += 1
    #     return i * i == num 

    # 二分查找
    # def isPerfectSquare(self, num):
    #     begin, end = 0, num
    #     while begin <= end:
    #         mid = (begin + end) / 2
    #         result = mid * mid
    #         if result == num:
    #             return True
    #         elif result > num:
    #             end = mid - 1
    #         else:
    #             begin = mid + 1
    #     return False

    # 等差数列
    def isPerfectSquare(self, num):
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(16))