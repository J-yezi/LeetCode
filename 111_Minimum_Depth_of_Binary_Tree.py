#coding=utf-8

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left != 0 and right != 0:
            return min(left, right) + 1
        return left + right + 1

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(2)

    print(s.minDepth(root))