#coding=utf-8

'''
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例:
输入：
s = "abcd"
t = "abcde"
输出：
e
解释：
'e' 是那个被添加的字母。
'''

class Solution:
    # 先转成ASCII码，然后相减，就是多添加的字符
    def findTheDifference(self, s, t):
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

if __name__ == "__main__":
    s = Solution()
    print(s.findTheDifference('abcd', 'abcde'))