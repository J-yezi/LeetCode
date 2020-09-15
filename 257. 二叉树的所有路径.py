"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。
说明: 叶子节点是指没有子节点的节点。

输出: ["1->2->5", "1->3"]
解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
"""


from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    递归
    思路是可以拆分成当前节点到根节点的路径是path，然后加上当前节点到叶子节点的路径
    1、判断node是否为空
    2、添加当前节点的值到path上面
    3、如果当前节点是叶子节点，那么路径就算完成了
    4、如果不是叶子节点，那么就就在路径上追加->
    5、当前节点非叶子节点，那么接着访问该节点的左子节点和右子节点
    """
    def binaryTreePaths1(self, root):
        paths = []

        def recurse(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    recurse(node.left, path)
                    recurse(node.right, path)

        recurse(root, '')
        return paths

    def binaryTreePaths2(self, root):
        if not root:
            return []

        paths = []
        nodes = deque([root])
        vals = deque([''])

        while nodes:
            node = nodes.popleft()
            path = vals.popleft()

            path += str(node.val)
            print("---", path)
            if not node.left and not node.right:
                paths.append(path)
                continue

            path += '->'
            if node.left:
                nodes.append(node.left)
                vals.append(path)
            if node.right:
                nodes.append(node.right)
                vals.append(path)
        return paths


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    node2.right = node4

    s = Solution()
    ans = s.binaryTreePaths2(node1)
    print(ans)
