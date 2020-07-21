#coding=utf-8

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例:
给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    迭代
    """
    # def swapPairs(self, head):
    #     if head is None or head.next is None:
    #         return head

    #     new = ListNode(0)
    #     prev = new
    #     while head and head.next:
    #         next = head.next.next

    #         prev.next = head.next
    #         prev.next.next = head

    #         head = next
    #         prev = prev.next.next
    #         prev.next = None
    #     prev.next = head
    #     return new.next

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    s = Solution()
    head = s.swapPairs(node1)

    while head is not None:
        print(head.val)
        head = head.next
