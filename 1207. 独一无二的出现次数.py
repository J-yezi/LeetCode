'''
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

示例 1：
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
'''


class Solution(object):
    def uniqueOccurrences(self, arr):
        dic, s = {}, set()
        for i in arr:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic.keys():
            if dic[i] in s:
                return False
            else:
                s.add(dic[i])
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.uniqueOccurrences([1, 2, 2, 1, 1, 3]))
