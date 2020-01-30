#coding=utf-8

'''
给定一个二叉树，返回它的 后序 遍历。
示例:
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 
输出: [3,2,1]
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
    # def postorderTraversal(self, root):
    #     array = []
    #     self.__post__(root, array)
    #     return array

    # def __post__(self, node, array):
    #     if not node: return
    #     self.__post__(node.left, array)
    #     self.__post__(node.right, array)
    #     array.append(node.val)

    '''
    迭代
    '''
    def postorderTraversal(self, root):
        if not root: return None
        array, stack = [], [root]
        while len(stack) > 0:
            node = stack.pop()
            array.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return array[::-1]

if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.right = node2
    node2.left = node3

    s = Solution()
    print(s.postorderTraversal(node1))