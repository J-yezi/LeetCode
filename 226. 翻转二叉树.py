#coding=utf-8

'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9

输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 递归
    # def invertTree(self, root):
        # if root is None: return None

        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)

        # root.right = left
        # root.left = right

        # return root
    
    # 迭代
    def invertTree(self, root):
        if root is None: return None

        stack = []
        stack.append(root)
        while stack != []:
            item = stack.pop()
            if item is not None:
                item.left, item.right = item.right, item.left
                stack.append(item.left)
                stack.append(item.right)
        return root

    
    def print(self, root):
        if root:
            print(root.val)
            self.print(root.left)
            self.print(root.right)

if __name__ == "__main__":
    node1 = TreeNode(4)
    node2 = TreeNode(2)
    node3 = TreeNode(7)
    node4 = TreeNode(1)
    node5 = TreeNode(3)
    node6 = TreeNode(6)
    node7 = TreeNode(9)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    s = Solution()
    s.invertTree(node1)
    s.print(node1)