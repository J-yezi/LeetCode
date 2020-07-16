#coding=utf-8

"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。
"""

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        
        index = 1
        curr = nums[0]
        while len(nums) > index:
            if nums[index] == curr:
                nums.remove(curr)
            else:
                curr = nums[index]
                index += 1
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([]))