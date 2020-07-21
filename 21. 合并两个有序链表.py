#coding=utf-8

'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 迭代
    # def mergeTwoLists(self, l1, l2):
    #     head = curr = ListNode(0)
    #     while l1 and l2:
    #         if l1.val > l2.val:
    #             curr.next = l2
    #             l2 = l2.next
    #         else:
    #             curr.next = l1
    #             l1 = l1.next
    #         curr = curr.next
    #     curr.next = l1 if l1 else l2
    #     return head.next

    # 递归
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

if __name__ == "__main__":
    node1 = ListNode(-9)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node1.next = node2
    # node2.next = node3

    node4 = ListNode(5)
    node5 = ListNode(7)
    node6 = ListNode(4)
    node4.next = node5
    # node5.next = node6

    s = Solution()
    head = s.mergeTwoLists(node1, node4)
    while head:
        print(head.val)
        head = head.next
