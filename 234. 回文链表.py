#coding=utf-8

'''
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true

进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 普通解法，将链表转换成数组，然后两头进行比较
    # def isPalindrome(self, head):
    #     arr = []
    #     while head is not None:
    #         arr.append(head.val)
    #         head = head.next
        
    #     h, e = 0, len(arr) - 1
    #     while h < e:
    #         if arr[h] != arr[e]:
    #             return False
    #         h += 1
    #         e -= 1
    #     return True

    '''
    双指针+反转
    利用快慢指针，迅速找到链表的中间
    在查找链表中间的过程，将前面的node反转
    最后将两个链表进行比较
    '''
    def isPalindrome(self, head):
        slow, fast, pre, prepre = head, head, None, None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
            pre.next = prepre
            prepre = pre

        # 链表的长度是个奇数   
        if fast:
            slow = slow.next

        while slow:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True
            

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(0)
    node3 = ListNode(1)
    # node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    # node3.next = node4

    s = Solution()
    print(s.isPalindrome(node1))