#coding=utf-8

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