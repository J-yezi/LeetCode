"""
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L)
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

示例 1:

输入:
    1
   / \
  0   2

  L = 1
  R = 2

输出:
    1
      \
       2
"""


from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def trimBST(self, node, low, high):
        if not node:
            return None

        left = self.trimBST(node.left, low, high)
        right = self.trimBST(node.right, low, high)

        if node.val < low:
            return right
        elif node.val > high:
            return left
        else:
            node.left = left
            node.right = right
            return node

    # 递归的另外一种写法
    def trimBST1(self, node, low, high):
        if not node:
            return node
        if node.val < low:
            return self.trimBST1(node.right, low, high)
        if node.val > high:
            return self.trimBST1(node.left, low, high)

        node.left = self.trimBST1(node.left, low, high)
        node.right = self.trimBST1(node.right, low, high)
        return node


if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(0)
    node3 = TreeNode(4)
    node4 = TreeNode(2)
    node5 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.right = node4
    node4.left = node5

    s = Solution()
    result = s.trimBST(node1, 1, 2)

    stack = deque([result])
    while stack:
        node = stack.popleft()
        if node:
            print(node.val)
            stack.append(node.left)
            stack.append(node.right)
