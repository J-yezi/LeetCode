'''
给定一个二叉树，返回它的 前序 遍历。
示例:
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # 递归
    def preorderTraversal1(self, root):
        array = []

        def recurse(node, array):
            if not node:
                return
            array.append(node.val)
            recurse(node.left, array)
            recurse(node.right, array)
        return array

    # 迭代
    def preorderTraversal(self, root):
        array, stack = [], [root]
        while len(stack) > 0:
            node = stack.pop()
            if node:
                array.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return array


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3

    s = Solution()
    print(s.preorderTraversal(node1))
