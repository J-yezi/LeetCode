#coding=utf-8

'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    '''
    递归
    思路：还是采用了前序遍历二叉树的方式，但是事先将层数的空数组添加到levels里面
    然后在递归中使用了level，然后将值添加到对应的数组中
    '''
    def levelOrder(self, root):
        levels = []
        if not root: return levels

        def helper(node, level):
            # 保证有几层，levels里面就有几个数组
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root, 0)
        return levels

    '''
    迭代
    '''
    # def levelOrder(self, root):
    #     if not root: return None
    #     array, stack = [], [root]
    #     while len(stack) > 0:
    #         temp_node, temp_array = [], []
    #         for n in stack:
    #             temp_array.append(n.val)
    #             if n.left: temp_node.append(n.left)
    #             if n.right: temp_node.append(n.right)
    #         stack = temp_node
    #         array.append(temp_array)
    #     return array

    

if __name__ == "__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node6 = TreeNode(4)
    node7 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    node2.left = node6
    node2.right = node7

    s = Solution()
    print(s.levelOrder(node1))