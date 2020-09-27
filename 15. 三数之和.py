"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            """
            这里利用了双指针方法
            我们固定了前两重循环枚举到的元素 aa 和 bb，那么只有唯一的 cc 满足a+b+c=0
            当第二重循环往后枚举一个元素 b'时，由于 b'>b，那么满足 a+b'+c'=0，一定有c'<c
            """
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                """
                虽然这里面还有一次while循环，其实当second等于third的时候，就退出循环了
                相对来说就只有一次循环
                原理是利用双指针一个从小到大遍历，一个从大到小遍历
                """
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum1([-1, 0, 1, 2, -1, -4]))
