'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

说明:
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。
'''


class Solution:
    '''
    使用额外的数组，通过计算循环后的位置，直接给数组对应的位置进行赋值
    '''
    # def rotate(self, nums, k):
    #     arr = [0 for _ in range(len(nums))]
    #     for i, n in enumerate(nums):
    #         arr[(i + k) % len(nums)] = n
    #     return arr

    '''
    使用环状替换
    里面的循环是用来按照k的递增，逐渐替换，例如1->3->5->7
    有可能按照这个循环，会构成一个环，1->3->5->1->3->5，这样不会处理2->-4->6，
    所有添加了外面的循环，注意是使用count < len(nums)，这样就能表示所有元素都进行了处理

    时间复杂度：O(n)O(n) 。只遍历了每个元素一次。
    空间复杂度：O(1)O(1) 。使用了常数个额外空间
    '''
    # def rotate(self, nums, k):
    #     k = k % len(nums)
    #     count, i = 0, 0
    #     while count < len(nums):
    #         index, curr = i, nums[i]
    #         while True:
    #             next = (index + k) % len(nums)
    #             curr, nums[next] = nums[next], curr
    #             count += 1
    #             index = next
    #             if i == index:
    #                 break
    #         i += 1
    #     return nums

    '''
    原始数组                  : 1 2 3 4 5 6 7
    反转所有数字后             : 7 6 5 4 3 2 1
    反转前 k 个数字后          : 5 6 7 4 3 2 1
    反转后 n-k 个数字后        : 5 6 7 1 2 3 4 --> 结果
    '''
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.rotate([-1, -100, 3, 99], 2))
