"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i in range(len(nums)):
            try:
                j = dic[nums[i]]
                if i - j <= k:
                    return True
                else:
                    dic[nums[i]] = i
            except Exception as e:
                _ = e
                dic[nums[i]] = i
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
