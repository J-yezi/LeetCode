'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000
'''


class Solution:
    """
    快速幂算法（递归）
    n是偶数，x^2就等于x^(n/2)次方再平方，如果是奇数，那么就还需要乘以x
    """
    # def fastPow(self, x, n):
    #     if n == 0:
    #         return 1
    #     temp = self.fastPow(x, n / 2)
    #     if n % 2 == 0:
    #         return temp * temp
    #     else:
    #         return temp * temp * x

    # def myPow(self, x, n):
    #     if n < 0:
    #         x = 1 / x
    #         n = -n
    #     return self.fastPow(x, n)

    """
    快速幂算法（循环）
    2^7就是2 * 2 * 2 * 2 * 2 * 2 * 2
            2 * 4 * 4 * 4
               2 * 4 * 8
    当为奇数的时候，直接乘x
    第一阶段，乘以x，此时x为2
    第二阶段，乘以x，此时x为4
    最后阶段，乘以x，此时x为8
    """
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            # n为奇数
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.myPow(2.000000, 10))
