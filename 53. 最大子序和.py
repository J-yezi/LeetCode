#coding=utf-8

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

class Solution:
    # def maxSubArray(self, nums):
    #     count = float('-inf')
    #     for i in range(len(nums)):
    #         temp = nums[i]
    #         max_temp = nums[i]
    #         for j in range(i + 1, len(nums)):
    #             temp = temp + nums[j]
    #             max_temp = max(max_temp, temp)
    #         count = max(count, max_temp)
    #     return count

    """
    思想就是当前面的序列加起来大于0，表示最大的序列有可能还在后面，但是当前面的序列小于0，那么表示最大的序列应该从当前值开始计算
    """
    def maxSubArray(self, nums):
        sum = 0
        ans = nums[0]
        for i in nums:
            if sum > 0:
                sum = sum + i
            else:
                sum = i
            ans = max(ans, sum)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))