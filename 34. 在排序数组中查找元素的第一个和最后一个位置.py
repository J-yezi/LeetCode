"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
"""


class Solution(object):
    def searchRange1(self, nums, target):
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target and first == -1:
                first = i
            if nums[i] == target:
                last = i
        return [first, last]

    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if not left:
                print("---", lo, mid, hi)
            if nums[mid] > target or (left and target == nums[mid]):
                # 注意这里是hi=mid 不是hi=mid-1，如果是已经查找target，那么可以继续下去，因为是hi=mid
                hi = mid
            else:
                lo = mid + 1

        return lo

    """
    二分查找
    先找第一个值，当如果target=nums[mid]，则hi = mid，表示还需要继续查找，如果能够了更前面的那么，lo的值取更小的
    当left_idx没找到值，那么right_idx肯定也是没有值
    当left_idx有值，那么
    """
    def searchRange2(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        right_idx = self.extreme_insertion_index(nums, target, False) - 1
        return [left_idx, right_idx]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange2([5, 7, 7, 8, 8, 10], 7))
