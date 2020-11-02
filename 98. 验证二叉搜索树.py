'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。
假设一个二叉搜索树具有如下特征：
节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def isValidBST(self, root):
    #     return self.isValidBSTHandler(root, float('-inf'), float('inf'))
    # """
    # 递归
    #         root
    #       /      \
    #     node1   node2
    #             /   \
    #         node3   node4
    # node3在node2的左边，那么就应该小于传递进来的max，并且大于root，
    # 而且min就是上一轮中root的val，所以min < node3 < max
    # """
    def isValidBSTHandler(self, root, min, max):
        if root is None:
            return True
        if not min < root.val < max:
            return False
        return self.isValidBSTHandler(root.left, min, root.val) and self.isValidBSTHandler(root.right, root.val, max)

    """
    和上面的递归方式差不多，只是逐层判断
    """
    def isValidBST(self, root):
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    node1 = TreeNode(15)
    node1.left = TreeNode(6)
    node1.right = TreeNode(20)
    root.right = node1

    s = Solution()
    print(s.isValidBST(root))
