#coding=utf-8

'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2
'''

class Solution:
    '''
    哈希表
    '''
    # def majorityElement(self, nums):
    #     dic = {}
    #     for i in nums:
    #         try:
    #             dic[i] += 1
    #         except:
    #             dic[i] = 1

    #     for key in dic.keys():
    #         if dic[key] > len(nums) / 2:
    #             return key
    #     return None

    '''
    排序
    那么数组最中间的数就肯定是众数了
    '''
    # def majorityElement(self, nums):
    #     nums.sort()
    #     return nums[len(nums) / 2]

    '''
    摩尔投票法
    众数出现的次数最多，所以即使其他数据的总和抵消了，最后的结果还是会大于0
    '''
    # def majorityElement(self, nums):
    #     candidate, count = 0, 0
    #     for i in nums:
    #         if count == 0:
    #             candidate = i
    #             count = 1
    #         elif candidate == i:
    #             count += 1
    #         else:
    #             count -= 1
    #     return candidate

    '''
    分治算法
    将数组拆分成左右两，然后针对左右两边继续进行拆分，直到力度为1，然后就对左右进行比较
    比较的方式就是看左右两边的数量，然后多的就结果返回，作为递归合并阶段的参数，继续进行比较
    '''
    def majorityElement(self, nums):
        def majority_element_rec(begin, end):
            if begin == end:
                return nums[begin]

            mid = (begin + end) // 2
            left = majority_element_rec(begin, mid)
            right = majority_element_rec(mid + 1, end)

            if left == right:
                return left
            
            left_count = sum(1 for i in range(begin, end + 1) if nums[i] == left)
            right_count = sum(1 for i in range(begin, end + 1) if nums[i] == right)
            return left if left_count > right_count else right
        return majority_element_rec(0, len(nums) - 1)

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))