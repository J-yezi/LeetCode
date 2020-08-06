"""
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""


class Solution(object):
    """
    子串逐一比较 - 线性时间复杂度
    """
    def strStr1(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1

    def strStr2(self, haystack, needle):
        L, n = len(needle), len(haystack)
        if L == 0:
            return 0

        pn = 0
        while pn < n - L + 1:
            while pn < n - L + 1 and haystack[pn] != needle[0]:
                pn += 1

            curr_len = pL = 0
            while pL < L and pn < n and haystack[pn] == needle[pL]:
                pn += 1
                pL += 1
                curr_len += 1

            if curr_len == L:
                return pn - L

            pn = pn - curr_len + 1

        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.strStr2("mississippi", "issip"))
