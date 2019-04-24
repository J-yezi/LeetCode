'''
给出两个非空的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        value = 0
        head = curr = ListNode(0)
        while l1 or l2:
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            curr.next = ListNode(value % 10)
            curr = curr.next
            value = value // 10

        if value > 0:
            curr.next = ListNode(value)
        return head.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next