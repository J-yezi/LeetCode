#coding=utf-8

'''
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false
'''

class Solution:
    '''
    普通方法，将映射关系保存在字典中，然后进行比较
    '''
    def wordPattern(self, pattern, str):
        dic, arr= {}, str.split(' ')
        if len(arr) != len(pattern): return False

        for i, s in enumerate(pattern):
            try:
                if dic[s] != arr[i]: return False
            except:
                dic[s] = arr[i]

        dic = {}
        for i, s in enumerate(arr):
            try:
                if dic[s] != pattern[i]: return False
            except:
                dic[s] = pattern[i]
        
        return True

if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern('abba', 'dog cat cat dog'))