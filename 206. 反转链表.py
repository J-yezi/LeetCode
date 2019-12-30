#coding=utf-8

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
    # 迭代法
    # def reverseList(self, head):
    #     temp = None
    #     while head is not None:
    #         curr = head
    #         head = head.next
    #         curr.next = temp
    #         temp = curr
    #     return temp

    def reverseList(self, head):
        if head is None or head.next is None: return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur

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
    head = s.reverseList(node1)
    while head is not None:
        print(head.val)
        head = head.next