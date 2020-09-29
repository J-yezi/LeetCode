"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，
使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        m = float('inf')
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            third = n - 1
            second = first + 1
            while second < third:
                if second > first + 1 and nums[second] == nums[second - 1]:
                    second += 1
                elif third < n - 1 and nums[third] == nums[third + 1]:
                    third -= 1
                else:
                    t = nums[first] + nums[second] + nums[third]
                    if t - target > 0:
                        third -= 1
                    else:
                        second += 1
                    if abs(target - t) < abs(target - m):
                        m = t
        return m


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, 4], 1))
