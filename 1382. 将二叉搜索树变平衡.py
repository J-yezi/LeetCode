"""
给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
构建平衡二叉树
1、进行中序遍历，将二叉搜索树转换成排序数组
2、利用每次访问最中间的节点，将排序数组转换成平衡二叉搜索树
"""


class Solution(object):
    def balanceBST(self, root):
        # 中序遍历
        def getInorder(o):
            if o.left:
                getInorder(o.left)
            inorderSeq.append(o.val)
            if o.right:
                getInorder(o.right)

        # 就是普通的构建二叉搜索树
        def build(left, right):
            # //是整数的除法
            mid = (left + right) // 2
            o = TreeNode(inorderSeq[mid])
            if left <= mid - 1:
                o.left = build(left, mid - 1)
            if mid + 1 <= right:
                o.right = build(mid + 1, right)
            return o

        inorderSeq = list()
        getInorder(root)
        return build(0, len(inorderSeq) - 1)


if __name__ == "__main__":
    pass
