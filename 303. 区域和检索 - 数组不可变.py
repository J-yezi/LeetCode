"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：
给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

说明:
你可以假设数组不可变。
会多次调用 sumRange 方法。
"""


class Solution:
    # 超出时间限制
    # def __init__(self, nums):
    #     self.nums = nums
    #     self.helper = {}
    #     for i in range(len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum += nums[j]
    #             self.helper[(i, j)] = sum

    # def sumRange(self, i, j):
    #     return self.helper[(i, j)]

    def __init__(self, nums):
        self.nums = nums
        self.helper = {}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.helper[i] = sum

    def sumRange(self, i, j):
        return self.helper[j] - (0 if i == 0 else self.helper[i - 1])


if __name__ == "__main__":
    s = Solution([-2, 0, 3, -5, 2, -1])
    print(s.sumRange(0, 2))
