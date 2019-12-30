#coding=utf-8

class Solution:
    # 暴力法
    # def isValid(self, s):
    #     stack = []
    #     for i in s:
    #         if i == '(':
    #             stack.append(i)
    #         else:
    #             if len(stack) == 0:
    #                 return False
    #             else:
    #                 stack.pop()
    #     return len(stack) == 0

    # def longestValidParentheses(self, s):
    #     max_len = 0
    #     for i in range(len(s)):
    #         for j in range(i + 2, len(s) + 1, 1):
    #             if self.isValid(s[i:j]):
    #                 max_len = max(j - i, max_len)
    #     return max_len

    """
    栈方法
    当整个栈为空的时候，最长的有效括号就断了
    栈底的元素就是有效括号被截断的元素位置
    当)匹配到中(，那么这两个字符中间的肯定也是有效的括号
    """
    # def longestValidParentheses(self, s):
    #     max_len = 0
    #     stack = [-1]
    #     for i in range(len(s)):
    #         if s[i] == '(':
    #             stack.append(i)
    #         else:
    #             stack.pop()
    #             if len(stack) == 0:
    #                 stack.append(i)
    #             else:
    #                 max_len = max(max_len, i - stack[-1])
    #     return max_len

    """
    动态规划
    """
    def longestValidParentheses(self, s):
        max_len = 0
        stack = [0 for n in range(len(s))]
        for i in range(len(s)):
            if s[i] == ')' and i > 0:
                if s[i - 1] == '(':
                    stack[i] = (stack[i - 2] if i >= 2 else 0) + 2
                elif i - stack[i - 1] > 0 and s[i - stack[i - 1] - 1] == '(':
                    stack[i] = stack[i - 1] + 2 + (stack[i - stack[i - 1] - 2] if i - stack[i - 1] >= 2 else 0)
                max_len = max(max_len, stack[i])
        return max_len

if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses('()(())'))