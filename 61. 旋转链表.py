#coding=utf-8

'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    解题思路：先获取到整个链表的长度，然后获取到n-k处的node，设置为head，并且将链表尾部的next设置为以前的head
    '''
    def rotateRight(self, head, k):
        if not head:
            return None
        if not head.next:
            return head

        n = 1
        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            n += 1

        old_tail.next = head
        k = k % n
        
        new_tail = head
        for i in range(n - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head



if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(0)
    node3 = ListNode(2)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node5

    s = Solution()
    new_head = s.rotateRight(node1, 4)
    while new_head:
        print(new_head.val)
        new_head = new_head.next

