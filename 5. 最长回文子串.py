#coding=utf-8

class Solution:
    """
    扩展中心
    回文串一定是对称的，所以我们可以每次循环选择一个中心，进行左右扩展，判断左右字符是否相等即可
    存在奇数的字符串和偶数的字符串，所以我们需要从一个字符开始扩展，或者从两个字符之间开始扩展，所以总共有n+n-1个中心
    """
    def longestPalindrome(self, s):
        if (s == None or len(s) < 1): return ''
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > right2 - left2:
                if right1 - left1 > end - start:
                    start = left1
                    end = right1
            else:
                if right2 - left2 > end - start:
                    start = left2
                    end = right2
        return s[start: end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (left + 1, right - 1)

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('babad'))