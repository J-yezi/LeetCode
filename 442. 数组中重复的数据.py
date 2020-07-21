#coding=utf-8

'''
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
找到所有出现两次的元素。
你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：
输入:
[4,3,2,7,8,2,3,1]
输出:
[2,3]
'''

class Solution:
    # 暴力法
    def findDuplicates(self, nums):
        dic = {}
        for i in nums:
            try:
                dic[i] += 1
            except:
                dic[i] = 1

        arr = []
        for key in dic.keys():
            if dic[key] == 2:
                arr.append(key)
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))