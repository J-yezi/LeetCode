"""
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
给定一个 整数 n， 如果他是完美数，返回 True，否则返回 False
"""


class Solution(object):
    """
    数学方法
    1、通过归纳，可以得出结论：如果i是num的因子，那么num/i是num的另外一个因子
    2、之前要找出所有的因子需要一直循环到num，但是现在i<=num的平方根，num/i>=num的平方根
    3、只需要循环到num的平方根就行了，减少了循环的次数
    """
    def checkPerfectNumber(self, num):
        if num <= 0:
            return False

        sum, i = 0, 1
        while i * i <= num:
            if num % i == 0:
                sum += i
                # 求另外一半的因子
                if i * i != num:
                    sum += num / i
            i += 1
        return sum == 2 * num


if __name__ == "__main__":
    s = Solution()
    print(s.checkPerfectNumber(28))
