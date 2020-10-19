'''
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
'''


import collections


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    '''
    迭代
    '''
    def connect1(self, root):
        if not root:
            return None
        stack = collections.deque([root])
        while stack:
            size = len(stack)
            for i in range(size):
                node = stack.popleft()
                if i < size - 1:
                    node.next = stack[0]
                if node.left and node.right:
                    stack.append(node.left)
                    stack.append(node.right)
        return root

    '''
    递归
    '''
    def connect(self, root):
        def recurse(node):
            if not node.left and not node.right:
                return
            node.left.next = node.right
            if node.next:
                node.right.next = node.next.left
            recurse(node.left)
            recurse(node.right)
        if not root:
            return None
        recurse(root)
        return root


if __name__ == "__main__":
    s = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    root = s.connect(node1)
    print(root.left.right.next.val)
