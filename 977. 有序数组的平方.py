"""
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
"""


class Solution(object):
    def quick_sort(self, left, right, array):
        if left > right:
            return
        low, high = left, right
        while left < right:
            while array[left] <= array[right] and left < right:
                right -= 1
            array[left], array[right] = array[right], array[left]
            while array[left] <= array[right] and left < right:
                left += 1
            array[left], array[right] = array[right], array[left]
        self.quick_sort(low, right - 1, array)
        self.quick_sort(right + 1, high, array)

    def sortedSquares(self, A):
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        self.quick_sort(0, len(A) - 1, A)
        return A

    def sortedSquares1(self, A):
        left, right = 0, len(A) - 1
        result = []
        while left <= right:
            if A[left] * A[left] < A[right] * A[right]:
                result.append(A[right] * A[right])
                right -= 1
            else:
                result.append(A[left] * A[left])
                left += 1
        return result[::-1]


if __name__ == "__main__":
    s = Solution()
    a = [-7, -3, 2, 3, 11]
    print(s.sortedSquares1(a))
