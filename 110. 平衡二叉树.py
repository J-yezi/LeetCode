'''
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:
给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    递归 从顶至底（暴力法）
    1、获取当前节点的左右最大深度，然后判断当前节点是否平衡
    2、上个条件成立的情况下，在判断左右子节点是否也平衡
    '''
    def isBalanced1(self, root):
        if not root:
            return True
        """
        最先判断是root是否是平衡二叉树
        然后再判断root.left和root.right是否是平衡二叉树
        会造成一个问题，就是在判断root的时候也会计算其他节点的深度
        这个过程中就会产生很多重复数据
        """
        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    # 获取当前节点的最大深度
    def depth1(self, root):
        if not root:
            return 0
        return max(self.depth1(root.left), self.depth1(root.right)) + 1

    def isBalanced2(self, root):
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
    def depth2(self, root):
        if not root:
            return 0
        # 先查找左子树，并且返回左子树的高度
        left = self.depth2(root.left)
        # 提前阻断，碰到左子树已经不是平衡二叉树，那么就提前结束
        if left == -1:
            return -1
        # 然后查找右子树的高度
        right = self.depth2(root.right)
        if right == -1:
            return -1
        '''
        比较当前节点的左子树和右子树是否满足平衡二叉树
        如果是平衡二叉树，那么就取当前节点的左右子树的最高+1
        如果不满足，则直接返回-1
        '''
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
