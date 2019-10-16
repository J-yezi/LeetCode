#coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归 从顶至底（暴力法）
    # def isBalanced(self, root):
    #     if not root: return True
    #     if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
    #         return self.isBalanced(root.left) and self.isBalanced(root.right)
    #     return False

    # def depth(self, root):
    #     if not root: return 0
    #     return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        return self.depth(root) != -1
        
    """
    从底至顶（提前阻断法）
    对二叉树做深度优先遍历DFS
    终止条件：当DFS越过叶子节点时，返回高度0
    返回值：
        从底至顶，返回以每个节点root为根节点的子树最大高度(左右子树中最大的高度值加1 max(left,right) + 1)
        当我们发现有一例 左/右子树高度差 ＞ 1 的情况时，代表此树不是平衡树，返回-1
    当发现不是平衡树时，后面的高度计算都没有意义了，因此一路返回-1，避免后续多余计算
    最差情况是对树做一遍完整的DFS，时间复杂度为O(N)
    """
    def depth(self, root):
        if not root: return 0
        left = self.depth(root.left)
        if left == -1: return -1
        right = self.depth(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1

if __name__ == '__main__':
    s = Solution()

    root = TreeNode(6)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(12)
    root.right.right.left = TreeNode(4)

    print(s.isBalanced(root))