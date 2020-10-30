class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    '''
    递归
    解题思路：如果一个树的左子树与右子树镜像对称，那么这个树是对称的
    该问题可以转化为：两个树在什么情况下互为镜像？

    如果同时满足下面的条件，两个树互为镜像：
    1、它们的两个根结点具有相同的值。
    2、每个树的右子树都与另一个树的左子树镜像对称。
    '''
    # def isSymmetric(self, root):
    #     # root为对称的话，那么root1.left和root1.right镜像，root1.left和root2.right也肯定是镜像
    #     return self.isMirror(root, root)

    # def isMirror(self, left, right):
    #     if left is None and right is None: return True
    #     if left is None or right is None: return False
    #     return (left.val == right.val) and
    # self.isMirror(left.right, right.left)
    # and self.isMirror(left.left, right.right)

    '''
    迭代
    解题思路：每次入栈的都是成对的，并且需要进行比较值是否相等
    然后入栈的就是(左子树的左节点，右子树的右节点)，(左子树的右节点，右子树的左节点)，
    并且分别以这两个节点作为新的镜像比较
    相当于将很大的一棵树逐渐拆分成一小块进行比较
    '''
    def isSymmetric(self, root):
        stack = [root, root]
        while stack:
            left = stack.pop(0)
            right = stack.pop(0)

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False

            stack.append(left.left)
            stack.append(right.right)

            stack.append(left.right)
            stack.append(right.left)
        return True


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node5 = TreeNode(4)
    node6 = TreeNode(4)
    node7 = TreeNode(3)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    s = Solution()
    print(s.isSymmetric(node1))
