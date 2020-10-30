'''
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。

示例 1:
输入: [1,2,3]
    1
   / \
  2   3
输出: 25
解释:
从根到叶子节点路径 1->2 代表数字 12.
从根到叶子节点路径 1->3 代表数字 13.
因此，数字总和 = 12 + 13 = 25.
'''


import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        def recurse(node, prev):
            if not root:
                return 0
            prev = prev * 10 + node.val
            if not node.left and not node.right:
                return prev
            else:
                return recurse(node.left, prev) + recurse(node.right, prev)
        return recurse(root, 0)

    def sumNumbers1(self, root):
        if not root:
            return 0
        stack = collections.deque([root])
        nums = collections.deque([root.val])
        total = 0
        while stack:
            node = stack.popleft()
            num = nums.popleft()
            if not node.left and not node.right:
                total += num
            else:
                if node.left:
                    stack.append(node.left)
                    nums.append(num * 10 + node.left.val)
                if node.right:
                    stack.append(node.right)
                    nums.append(num * 10 + node.right.val)
        return total


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    s = Solution()
    print(s.sumNumbers1(node1))
