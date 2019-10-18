#coding=utf-8

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
        if root is None: return True
        if not min < root.val < max: return False
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
    print(s.isValidBST1(root))