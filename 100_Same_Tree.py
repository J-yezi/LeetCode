#coding=utf-8

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isSameTree(self, p, q):
    #     # 当p and q都为None
    #     if p == q:
    #         return True
    #     try:
    #         if p.val == q.val:
    #             return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     except:
    #         return False
    #     return False

    def isSameTree(self, p, q):
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True


if __name__ == '__main__':
    s = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)

    q = TreeNode(1)
    q.right = TreeNode(2)

    print(s.isSameTree(p, q))