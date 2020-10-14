'''
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        def recurse(node, array):
            if not node:
                return
            recurse(node.left, array)
            array.append(node.val)
            recurse(node.right, array)

        array = []
        recurse(root, array)
        minVal, i = float('inf'), 0
        while i + 1 < len(array):
            minVal = min(minVal, abs(array[i] - array[i + 1]))
            i += 1
        return minVal

    def getMinimumDifference1(self, root):
        pre, minVal = -1, float('inf')

        def recurse(root):
            nonlocal pre, minVal
            if not root:
                return
            recurse(root.left)
            if pre != -1:
                minVal = min(minVal, abs(pre - root.val))
            pre = root.val
            recurse(root.right)
        recurse(root)
        return minVal


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(4)
    node3 = TreeNode(2)

    node1.right = node2
    node2.left = node3

    s = Solution()
    print(s.getMinimumDifference1(node1))
