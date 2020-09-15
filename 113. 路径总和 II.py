"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum1(self, root, sum):
        if not root:
            return []

        nodes = deque([root])
        vals = deque([[]])
        paths = []

        while nodes:
            node = nodes.popleft()
            path = vals.popleft()

            path.append(node.val)
            if not node.left and not node.right:
                count = 0
                for i in range(len(path)):
                    count += path[i]
                if count == sum:
                    paths.append(path)
                continue

            if node.left:
                nodes.append(node.left)
                vals.append(path[:])
            if node.right:
                nodes.append(node.right)
                vals.append(path[:])
        return paths


if __name__ == "__main__":
    node1 = TreeNode(5)
    node2 = TreeNode(4)
    node3 = TreeNode(8)
    node4 = TreeNode(11)
    node5 = TreeNode(13)
    node6 = TreeNode(4)
    node7 = TreeNode(7)
    node8 = TreeNode(2)
    node9 = TreeNode(1)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.left = node5
    node3.right = node6
    node4.left = node7
    node4.right = node8
    node6.right = node9

    s = Solution()
    print(s.pathSum1(node1, 22))
