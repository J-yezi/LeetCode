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
    回朔法+剪枝
    1、左括号的数量<输入的参数
    2、同时右节点的数量<输入的参数
    3、左括号的数量>右括号的数量
    '''
    def generateParenthesis(self, n):
        ans = []
        def backtrack(s = '', left = 0, right = 0):
            # 递归出口
            if len(s) == 2 * n:
                ans.append(s)
                return
            # 其实两个if就是在剪枝，右括号需要比左括号少才能放置右括号
            if left < n:
                """
                这里并没有像下面的方法进行回溯，主要是因为我传入的s是一个字符串，每次递归还原之后，方法的调用栈也会还原
                下面使用数组，所以整个过程中，都是使用一个引用
                但是方法栈还原后，s就会变成未添加最后一个括号的情况，相当于是进行了回溯
                """
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)
        backtrack()
        return ans

    """
    回朔法
    """
    # def generateParenthesis(self, n: int) -> [str]:
    #     def generate(A):
    #         if len(A) == 2*n:
    #             if valid(A):
    #                 ans.append("".join(A))
    #         else:
    #             # 当前位置，我先左括号的添加，然后探索剩下的解，然后进行回溯，将当前位置变成右括号，然后进行探索，最后又进行回溯，这样就能够找出所有括号的解
    #             A.append('(')
    #             # 当前位置添加左括号，然后在继续探索接下来的解
    #             generate(A)
    #             # 当前位置可以是右括号，所以需要进行回溯
    #             A.pop()
    #             A.append(')')
    #             # 添加右括号，然后继续探索接下来的解
    #             generate(A)
    #             # 然后又进行回溯
    #             A.pop()

    #     def valid(A):
    #         bal = 0
    #         for c in A:
    #             if c == '(': bal += 1
    #             else: bal -= 1
    #             if bal < 0: return False
    #         return bal == 0

    #     ans = []
    #     generate([])
    #     return ans

if __name__ == "__main__":
    s = Solution()
    arr = s.generateParenthesis(3)
    print(arr, len(arr))