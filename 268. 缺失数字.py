"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数

示例 1:
输入: [3,0,1]
输出: 2
"""


class Solution:
    """
    哈希表
    集合的插入操作的时间复杂度都是O(1)，一共插入了n个数，时间复杂度为O(n)
    集合的查询操作的时间复杂度同样是O(1)，最多查询n+1次，时间复杂度为O(n)
    """
    # def missingNumber(self, nums):
    #     nums_set = set(nums)
    #     for i in range(len(nums_set) + 1):
    #         if i not in nums_set:
    #             return i
    #     return None

    """
    位运算
    0-n中间缺少一个数，所以数组下标是0-(n-1)
    missing为n
    0-(缺少的一个数)-n和0-n进行异或，自然就找出了缺少的数
    """
    # def missingNumber(self, nums):
    #     missing = len(nums)
    #     for i, num in enumerate(nums):
    #         missing ^= i ^ num
    #     return missing

    """
    数学方法
    """
    def missingNumber(self, nums):
        experct = sum([n for n in range(len(nums) + 1)])
        actual = 0
        for num in nums:
            actual += num
        return experct - actual


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
