#coding=utf-8

'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
'''

class Solution:
    def combinationSum(self, candidates, target):
        self.getcombinationSum(candidates, [], 0, target)
        pass

    def getcombinationSum(self, candidates, prefix, curr, target):
        for i in candidates:
            if curr + i == target:
                prefix.append(i)
                return
            elif curr + i > target:
                return
            else:
                prefix.append(i)
                curr = curr + i
                self.getcombinationSum(candidates, prefix, curr, target)

if __name__ == '__main__':
    s = Solution()
    print