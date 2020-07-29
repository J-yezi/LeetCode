# coding=utf-8

"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    递归
    利用递归让left指向m的节点，right指向right的节点
    然后left和right之间交换值
    因为递归特性，right会向左移动，那么需要自己设置left向右移动
    直到left和right相等，或者left在right的右边
    """
    def reverseBetween1(self, head, m, n):
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            """
            利用递归，让left指向m位置的节点，然后让right指向n位置的节点
            """
            if n == 1:
                return
            right = right.next
            if m > 1:
                left = left.next

            recurseAndReverse(right, m - 1, n - 1)

            """
            利用递归进行回溯，回溯的时候其实就是right指针向后移动的过程
            """
            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val
                """
                left和right之间交换值，然后因为利用递归的特性，right会往后移动，那么left也需要向前移动
                """
                left = left.next

        recurseAndReverse(right, m, n)
        return head

    def reverseBetween2(self, head, m, n):
        if not head:
            return None

        cur, prev = head, None
        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # tail指向m的节点，con指向m节点的上一个节点
        tail, con = cur, prev
        # 从m到n的所有节点反转，prev指向n节点，cur指向n节点的下一个节点
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        if con:
            # m节点的上一个节点就需要和反转后的链表head进行拼接
            con.next = prev
        else:
            # 有可能是直接从第一个节点就就开始反转
            head = prev

        # tail需要和n节点后的节点进行拼接
        tail.next = cur
        return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Solution()
    head = s.reverseBetween1(node1, 2, 3)

    while head:
        print(head.val)
        head = head.next
