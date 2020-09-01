"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0
如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。
给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
输入:
    2
   / \
  2   5
     / \
    5   7

输出: 5
说明: 最小的值是 2 ，第二小的值是 5 。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        节点没有子节点，那么就取当前节点的值，如果当前节点的值等于root的值，那么当前值就为-1
        如果当前节点比root的值大，那么就直接return，起到提前剪枝的目的
        举个例子
             2
            / \
            -1   5
                / \
                5   7
        """
        def recusion(root, val):
            if not root:
                return -1

            if root.val > val:
                return root.val

            left = recusion(root.left, val)
            right = recusion(root.right, val)
            if left < 0:
                return right
            if right < 0:
                return left
            return min(left, right)
        return recusion(root, root.val)


if __name__ == "__main__":
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node4 = TreeNode(5)
    node5 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5

    s = Solution()
    print(s.findSecondMinimumValue(node1))
