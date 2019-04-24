class Solution:
    # 利用两次for循环处理
    # def twoSum(self, nums, target):
    #     for i, num_i in enumerate(nums):
    #         for j, num_j in enumerate(nums):
    #             if num_i + num_j == target:
    #                 return [i, j]
    #     return None

    # 对上面方法进行改进，利用hashmap来节省一次for循环
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            aother = target - num
            if aother in hashmap:
                return [hashmap[aother], index]
            hashmap[num] = index
        return None


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 13], 9))

