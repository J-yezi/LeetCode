#coding=utf-8

'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution(object):
    '''
    递归+剪枝
    1、左括号的数量<输入的参数
    2、同时右节点的数量<输入的参数
    3、左括号的数量>右括号的数量
    '''
    # def generateParenthesis(self, n):
    #     ans = []
    #     def backtrack(s = '', left = 0, right = 0):
    #         if len(s) == 2 * n:
    #             ans.append(s)
    #             return
    #         if left < n:
    #             backtrack(s + '(', left + 1, right)
    #         if right < left:
    #             backtrack(s + ')', left, right + 1)
    #     backtrack()
    #     return ans

    '''
    动态规划
    思路：n = (n - 1) + 1，在n-1对括号情况下，添加一对括号就行了
    怎么添加：n-1对括号要么添加在新括号里面，或者就是添加在新括号的右侧，为什么只有右侧，()()、(())()和()(())，右侧和左侧情况是一样的
    简化出来的公式：([0、1、2...对括号]) + [n-1、n-2、n-1-x剩余的括号]，(())() -> 里面一对括号，右侧一对括号，()(()) -> 里面0对括号，右侧两种括号，所以这里印证了右侧和左侧情况是一样的，只需要一种就行了
    循环：剩下的就是i(新加括号里面)+j(括号右侧)=n-1对括号，分别对i=0,j=n-1，的情况进行循环处理，然后对i=1,j=n-2的情况进行循环处理...依次类推
    '''
    def generateParenthesis(self, n):
        if n == 0: return []
        total = []
        total.append([None])
        total.append(['()'])
        for i in range(2,n + 1):
            l = []
            for j in range(i):
                list1 = total[j]
                list2 = total[i - 1 - j]
                for k1 in list1:
                    for k2 in list2:
                        if k1 is None:
                            k1 = ''
                        if k2 is None:
                            k2 = ''
                        l.append('(' + k1 + ')' + k2)
            total.append(l)
        return total[n]     

if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(3))