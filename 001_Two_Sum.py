'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标
'''

class Solution:
    '''
    利用两次for循环处理
    '''
    # def twoSum(self, nums, target):
    #     for i, num_i in enumerate(nums):
    #         for j, num_j in enumerate(nums):
    #             if num_i + num_j == target:
    #                 return [i, j]
    #     return None

    '''
    利用map来存储之前的元素，当碰到当前元素和目标元素=target的时候，就找到了
    相比较两次for循环来说，时间复杂度下降了，利用map来进行元素的筛选会比list进行for要快
    '''
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another = target - num
            if another in hashmap:
                return [hashmap[another], index]
            hashmap[num] = index
        return None


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 13], 9))

