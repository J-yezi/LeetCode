#coding=utf-8

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    其实和两个数组查找相同元素一样，都可以将其中一个数组用字典保存，然后遍历另外一个数组，进行查找，时间复杂度就会减少
    '''
    # def getIntersectionNode(self, headA, headB):
    #     dic = {}
    #     while headA is not None:
    #         dic[headA] = headA
    #         headA = headA.next
        
    #     while headB is not None:
    #         try:
    #             return dic[headB]
    #         except:
    #             pass
    #         headB = headB.next
    #     return None

    '''
    指针 pA 指向 A 链表，指针 pB 指向 B 链表，依次往后遍历
    如果 pA 到了末尾，则 pA = headB 继续遍历
    如果 pB 到了末尾，则 pB = headA 继续遍历
    比较长的链表指针指向较短链表head时，长度差就消除了
    如此，只需要将最短链表遍历两次即可找到位置
    '''
    def getIntersectionNode(self, headA, headB):
        tempA, tempB = headA, headB
        while tempA != tempB:
            tempA = tempA.next if tempA else headB
            tempB = tempB.next if tempB else headA
        return tempA

if __name__ == "__main__":
    node1 = ListNode(4)
    node2 = ListNode(1)
    node3 = ListNode(5)
    node4 = ListNode(0)
    node5 = ListNode(1)
    node6 = ListNode(8)
    node7 = ListNode(4)
    node8 = ListNode(5)
    
    # node1.next = node2
    # node2.next = node6
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6
    # node6.next = node7
    # node7.next = node8
    
    s = Solution()
    print(s.getIntersectionNode(node1, node3).val)