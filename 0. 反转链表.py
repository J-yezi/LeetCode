class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def __init__(self):
        self.h = None

    def reverse(self, head):
        if head.next is None:
            self.h = head
            return head
        temp = self.reverse(head.next)
        temp.next = head
        head.next = None
        return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)

    node1.next = node2
    node2.next = node3

    s = Solution()
    s.reverse(node1)

    while s.h:
        print(s.h.val)
        s.h = s.h.next
