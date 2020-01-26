#coding=utf-8

'''
给定一个二叉树，返回它的中序 遍历。
示例:
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    递归
    '''
    # def inorderTraversal(self, root):
    #     array = []
    #     self.__middle__(root, array)
    #     return array

    # def __middle__(self, node, array):
    #     if not node: return
    #     self.__middle__(node.left, array)
    #     array.append(node.val)
    #     self.__middle__(node.right, array)

    '''
    迭代
    '''
    def inorderTraversal(self, root):
        array, stack = [], []
        curr = root
        while len(stack) > 0 or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            array.append(curr.val)
            curr = curr.right
        return array

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3

    s = Solution()
    print(s.inorderTraversal(node1))