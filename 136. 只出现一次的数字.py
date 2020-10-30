'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1
'''


class Solution:
    # 普通方式
    # def singleNumber(self, nums):
    #     dic = {}
    #     for i in nums:
    #         try:
    #             dic.pop(i)
    #         except:
    #             dic[i] = 1
    #     return dic.popitem()[0]

    # 数学方法
    # def singleNumber(self, nums):
    #     return 2 * sum(set(nums)) - sum(nums)

    # 位运算
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            # 异或，相同位0，不同位1
            a ^= i
        return a


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1, 2, 1, 4, 2]))
