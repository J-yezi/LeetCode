#coding=utf-8

'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
'''

class Solution:
    def isPalindrome(self, s):
        p1, p2 = 0, len(s) - 1
        while p1 < p2:
            if s[p1].isalnum() and s[p2].isalnum():
                if s[p1].lower() != s[p2].lower():
                    return False
                else:
                    p1 += 1
                    p2 -= 1
            else:
                if not s[p1].isalnum():
                    p1 += 1
                if not s[p2].isalnum():
                    p2 -= 1
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama'))