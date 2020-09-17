# coding=utf-8

'''
给定一个链表，判断链表中是否有环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    哈希表
    判断当前指针是否在表中，如果有，那么就表示存在环
    """
    def hasCycle1(self, head):
        dic = {}
        pos = head
        while pos:
            try:
                dic[pos]
                return True
            except Exception as e:
                _ = e
                dic[pos] = pos
            pos = pos.next
        return False

    """
    设立慢指针和快指针。慢指针从head开始走，快指针从head的下一个开始走
    慢指针1次走1步，快指针1次走2步。如果快指针一直没有走到为nil，则当慢指针走了n步。快指针走了2n步，他们一定会汇合
    和操场跑圈圈差不多，跑得快的始终会超圈追上跑的慢的
    """
    def hasCycle2(self, head):
        try:
            fast = head.next.next
            slow = head.next
            while fast != slow:
                fast = fast.next.next
                slow = slow.next
            return True
        except Exception as e:
            _ = e
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
    print(s.hasCycle2(node1))
