#coding=utf-8

'''
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度
'''

import time

class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     value = 0
    #     keys = set()
    #     ls = len(s)
    #     for i in range(ls):
    #         temp = 0
    #         keys.clear()
    #         for j in range(i, ls):
    #             if not s[j] in keys:
    #                 keys.add(s[j])
    #                 temp += 1
    #             else: break
    #         value = max(value, temp)
    #     return value

    '''
    从0到j处理字符串，而不是从j到len(s)
    利用st来记录，上一个重复字符串的位置(i = max(st[s[j]], i))
    i的目的是记录当前字符最近一次重复字符的位置(不一定是当前字符重复，可能是其他字符重复)

    利用map来记录当前字符上一次出现位置，然后在找到这段字符串当中还有没有其他字符的上一次重复位置i
    这样保证了，从当前字符到i这个位置的字符串中是不存在重复字符的，然后使用ans来记录最大值
    '''
    def lengthOfLongestSubstring(self, s):
        st = {}
        i, ans = 0, 0
        for j, key in enumerate(s):
            if key in st:
                i = max(st[key], i)
            ans = max(ans, j - i + 1)
            st[key] = j + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    start = time.time()
    print(s.lengthOfLongestSubstring("abba"))
