#coding=utf-8

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
        if n == 1:
            return 1

        step1 = 1
        step2 = 2
        for i in range(2, n):
            temp = step2
            step2 = step1 + step2
            step1 = temp
        return step2

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(4))