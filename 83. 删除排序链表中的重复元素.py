'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    head = s.deleteDuplicates(node1)
    while head:
        print(head.val)
        head = head.next
