"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def index(self, array, target):
        i = 0
        while i < len(array):
            if array[i] == target:
                return i
            i += 1
        return i

    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        val = postorder[-1]
        i = self.index(inorder, val)
        node = TreeNode(val)
        node.left = self.buildTree(inorder[:i], postorder[:i])
        node.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return node


if __name__ == "__main__":
    s = Solution()
    node = s.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(node.val)
    print(node.left.val)
    print(node.right.right.val)
