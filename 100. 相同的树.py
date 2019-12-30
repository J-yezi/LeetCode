#coding=utf-8

'''
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:
输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true

示例 2:
输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
'''

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