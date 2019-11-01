#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def hasCycle(self, head):
    #     dic = {}
    #     pos = head
    #     while pos is not None:
    #         try:
    #             dic[pos]
    #             return True
    #         except:
    #             dic[pos] = pos
    #         pos = pos.next
    #     return False

    """
    设立慢指针和快指针。慢指针从head开始走，快指针从head的下一个开始走。慢指针1次走1步，快指针1次走2步。如果快指针一直没有走到为nil，则当慢指针走了n步。快指针走了2n步，他们一定会汇合
    """
    def hasCycle(self, head):
        try:
            fast = head.next.next
            slow = head.next
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except:
            return False

if __name__ == "__main__":
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    s = Solution()
    print(s.hasCycle(node1))
