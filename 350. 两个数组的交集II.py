'''
给定两个数组，编写一个函数来计算它们的交集。
示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
'''


class Solution:
    # 双指针方法
    def intersect1(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0

        arr = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                arr.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
