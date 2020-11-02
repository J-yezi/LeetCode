'''
给定两个数组，编写一个函数来计算它们的交集。

示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]
'''


class Solution:
    def intersection1(self, nums1, nums2):
        s = set()
        for i in nums1:
            s.add(i)

        arr = set()
        for i in nums2:
            if i in s:
                arr.add(i)
        return list(arr)

    '''
    排序+双指针
    '''
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i, j, s = 0, 0, set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                s.add(nums2[j])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return list(s)


if __name__ == "__main__":
    s = Solution()
    print(s.intersection([1, 2, 2, 1], [2, 2]))
