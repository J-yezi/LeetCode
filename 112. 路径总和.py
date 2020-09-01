"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum1(self, root, sum):
        if not root:
            return False
        que_node = deque([root])
        que_val = deque([root.val])

        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            # 判断当前叶子节点是否满足条件
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            # 将当前节点的左子节点入栈
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
            return False

    """
    递归
    大问题是根节点到叶子节点的路径总和
    小问题是跟节点到当前节点的总和是val，需要判断当前节点到叶子节点的总和是sum-val
    """
    def hasPathSum2(self, root, sum):
        # 当前节点是空，那么返回False
        if not root:
            return False
        # 当前节点是叶子节点，那么直接判断sum和节点的值即可
        if not root.left and not root.right:
            return sum == root.val
        # 当前节点是非叶子节点，只需要递归的判断当前节点的子节点是否满足条件即可
        return self.hasPathSum2(root.left, sum - root.val) or \
            self.hasPathSum2(root.right, sum - root.val)


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
    print(s.hasPathSum2(node1, 22))
