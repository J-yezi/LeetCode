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


from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    递归，有返回值
    自下而上
    1、先访问root的左节点，并且返回左节点
    2、然后访问root的右节点，并且返回右节点
    3、左节点和右节点都访问完后，再交换左右节点
    4、完成交换后，并且返回当前节点，然后回到上一层
    """
    def invertTree(self, root):
        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.right, root.left = left, right

        return root

    def invertTree1(self, root):
        def reverse(node):
            if node:
                node.left, node.right = node.right, node.left
                reverse(node.left)
                reverse(node.right)
        reverse(root)
        return root

    # 迭代
    def invertTree2(self, root):
        if not root:
            return None

        stack = deque([root])
        while stack:
            item = stack.popleft()
            if item:
                item.left, item.right = item.right, item.left
                stack.append(item.left)
                stack.append(item.right)
        return root

    def print(self, root):
        stack = deque([root])
        while stack:
            node = stack.popleft()
            if node:
                print(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)


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
    s.invertTree1(node1)
    s.print(node1)
