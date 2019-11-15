#coding=utf-8

'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
'''

class Solution:
    def intersection(self, nums1, nums2):
        s = set()
        for i in nums1:
            s.add(i)
        
        arr = set()
        for i in nums2:
            if i in s:
                arr.add(i)
        return list(arr)

if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1,2,2,1], [2,2]))