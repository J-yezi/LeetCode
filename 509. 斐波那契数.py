#coding=utf-8

class Solution(object):
    def fib(self, N):
        f0, f1, f2 = 0, 1, 0
        if N == 0 or N == 1: return N

        for _ in range(2, N + 1):
            f2 = f1 + f0
            f0 = f1
            f1 = f2
        return f2

if __name__ == "__main__":
    s = Solution()
    print(s.fib(4))
