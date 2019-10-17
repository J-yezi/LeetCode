#coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    # def maxDepth(self, root):
    #     if root is None:
    #         return 0
    #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root):
        stack = []
        if root is not None:
            stack.append((root, 1))

        depth = 0
        while stack != []:
            root, curr_depth = stack.pop()
            if root is not None:
                stack.append((root.left, curr_depth + 1))
                stack.append((root.right, curr_depth + 1))
                depth = max(depth, curr_depth)
        return depth

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)

    s = Solution()
    print(s.maxDepth(root))