'''
插入排序算法：
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

示例 1：
输入: 4->2->1->3
输出: 1->2->3->4
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        if head is None:
            return None
        helper = ListNode(-1000)
        pre, curr = helper, head

        '''
        1、新建一个prev节点，此时相当于已经有了两个链表，一个是prev的链表，一个是原来的链表
        2、以prev节点和后面的节点进行比较，如果大于curr或者prev链表已经到最后了，那么就将curr节点添加到prev链表中
        3、因为事先就存储了curr的next节点，所有可以直接从curr.next又开始进行比较
        4、方法中全部使用的.next进行比较的，那么带来的好处就是不用在存储prev和curr这样，需要存储两个节点，才能进行移除
        5、原始链表中curr一直都是链表头，直接将curr设置到prev链表中，相当于就是将curr直接从原始链表中移除
        '''
        while curr:
            next_step = curr.next
            while pre.next and pre.next.val < curr.val:
                pre = pre.next
            # 将curr插入到prev后面，因为prev的next比curr大
            curr.next = pre.next
            pre.next = curr
            pre = helper
            curr = next_step
        return helper.next

    # def insertionSortList(self, head):
        # if not head or not head.next: return head

        # prev = head
        # curr = head.next
        # while curr:
        #     node = head
        #     node_prev = None
        #     while curr != node:
        #         if node.val > curr.val:
        #             value = curr.val
        #             curr = self.__remove(prev, curr)
        #             head = self.__insert_head(head, node_prev, ListNode(value))
        #             break
        #         node_prev = node
        #         node = node.next
        #     prev = curr
        #     curr = curr.next
        # return head

    # def __remove(self, prev, curr):
    #     prev.next = curr.next
    #     return prev

    # def __insert_head(self, head, prev, curr):
    #     if prev:
    #         curr.next = prev.next
    #         prev.next = curr
    #         return head
    #     else:
    #         curr.next = head
    #         return curr


if __name__ == "__main__":
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(0)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    s = Solution()
    head = s.insertionSortList(node1)
    while head:
        print(head.val)
        head = head.next

