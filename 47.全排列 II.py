#coding=utf-8

class Solution:
    def permuteUnique(self, nums):
        res = []
        self.perm(res, nums, 0)
        return res
    
    """
    回溯法
    1、依次将第一个和后面的元素进行交换，然后在对后面的n-1进行全排列
    2、固定第一个，然后对后面的元素进行全排列，1+(n-1)
    3、全排列完后，在交换回来
    """
    def perm(self, res, nums, begin):
        if begin == len(nums):
            res.append(list(nums))
            return

        appeared = set()
        for i in range(begin, len(nums)):
            if nums[i] in appeared:
                continue
            appeared.add(nums[i])
            nums[i], nums[begin] = nums[begin], nums[i]
            self.perm(res, nums, begin + 1)
            nums[i], nums[begin] = nums[begin], nums[i]

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1, 1, 2]))