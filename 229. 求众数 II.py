'''
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:
输入: [3,2,3]
输出: [3]

示例 2:
输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
'''


class Solution:
    '''
    摩尔投票的变种类型
    找次数大于n / 3，那么数组中最多就两个这样的数
    那么我们就选举两个候选人
    出现A和B的时候，不进行处理，只有当另外的数，才进行减1操作，和摩尔投票一样的思路
    最后对这两个候选人进行一次判断，有可能只有一个候选人
    '''
    def majorityElement(self, nums):
        candidateA, countA, candidateB, countB = 0, 0, 0, 0
        for i in nums:
            if i == candidateA:
                countA += 1
                continue
            if i == candidateB:
                countB += 1
                continue

            if countA == 0:
                candidateA = i
                countA = 1
                continue
            if countB == 0:
                candidateB = i
                countB = 1
                continue
            countA -= 1
            countB -= 1

        countA, countB = 0, 0
        for i in nums:
            if i == candidateA:
                countA += 1
            elif i == candidateB:
                countB += 1

        res = []
        if countA > len(nums) / 3:
            res.append(candidateA)
        if countB > len(nums) / 3:
            res.append(candidateB)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
