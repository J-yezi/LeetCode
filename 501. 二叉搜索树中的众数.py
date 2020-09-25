"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2]

提示：如果众数超过1个，不需考虑输出顺序
进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        currentVal = 0
        maxCount = 0
        valList = []
        currentCount = 0

        def reverse(node):
            nonlocal currentVal, maxCount, valList, currentCount

            if not node:
                return
            reverse(node.left)

            if currentVal == node.val:
                currentCount += 1
            else:
                currentVal = node.val
                currentCount = 1

            if currentCount == maxCount:
                valList.append(currentVal)
            elif currentCount > maxCount:
                valList = []
                valList.append(currentVal)
                maxCount = currentCount

            reverse(node.right)

        reverse(root)
        return valList


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(2)

    node1.left = node2
    node2.right = node3

    s = Solution()
    print(s.findMode(node1))
