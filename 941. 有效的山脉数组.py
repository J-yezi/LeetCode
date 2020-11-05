'''
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
'''


class Solution(object):
    def validMountainArray1(self, A):
        if len(A) < 3:
            return False
        isAsc = True
        for i in range(len(A) - 1):
            if isAsc:
                if A[i + 1] < A[i]:
                    if i > 0:
                        isAsc = False
                    else:
                        return False
            else:
                if A[i + 1] >= A[i]:
                    return False
        return not isAsc

    def validMountainArray(self, A):
        if len(A) < 3:
            return False
        i, j = 0, len(A) - 1
        while A[i] < A[i + 1] and i + 2 < len(A):
            i += 1
        while A[j] < A[j - 1] and j > 0:
            j -= 1
        if j == i and j < len(A) - 1 and i > 0:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.validMountainArray([4, 5, 6, 7]))
