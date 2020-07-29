# coding=utf-8

'''
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    迭代法
    """
    def reverseList1(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

    """
    递归法
    利用递归来实现向后的指针，递归中的回溯可以帮助我们模拟一个指针从第nn个结点向中心移动的移动过程
    """
    def reverseList2(self, head):
        if head.next is None:
            return head

        # 其实递归回来每次返回的都是最后一个节点，也就是反转链表的新节点
        cur = self.reverseList2(head.next)
        # head的下一个节点，指向head
        head.next.next = head
        # 取消head之前指向下一个节点的关系
        head.next = None
        return cur

    """
    替换节点值
    先递归让right指向链表的尾部，然后利用递归的回溯，right指针逐渐往左移动
    让给left指针向右移动，然后逐渐和right指向的值进行交换
    """
    def reverseList3(self, head):
        left, right = head, head
        stop = False

        def reverse(right):
            nonlocal left, stop
            if right is None:
                return right

            reverse(right.next)
            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val
                left = left.next

        reverse(right)
        return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    head = s.reverseList3(node1)
    while head is not None:
        print(head.val)
        head = head.next
