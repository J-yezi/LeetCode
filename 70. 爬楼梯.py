#coding=utf-8

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
'''

class Solution:
    """
    记忆化递归
    第10个台阶的总的走的方式，就应该是第9个台阶的方式+第8个台阶的方式，因为在第8个台阶的时候，可以走2，在第9台阶，可以走1，
    但是第8个台阶的时候，不能在走1了，不然就包含在了第9个台阶的方式里面
    C在里面的用处就是保存已经存在的台阶的方式
    """
    # C = {}

    # def climbStairs(self, n):
    #     if n == 1:
    #         return 1
    #     elif n == 2:
    #         return 2
    #     if n in Solution.C:
    #         return Solution.C[n]
    #     else:
    #         result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #         Solution.C[n] = result
    #         return result

    def climbStairs(self, n):
        prev, curr = 0, 1
        for _ in range(n):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))