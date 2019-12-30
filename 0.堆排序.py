class Heap:
    def __init__(self, array):
        self.array = array

    def adjust_heap(self, i, size):
        left_child, right_child = 2 * i + 1, 2 * i + 2
        current_node = i
        # i超过了size/2，表示已经是叶子节点了
        # 从下往上进行调整
        if i < size / 2:
            if left_child < size and self.array[left_child] > self.array[current_node]:
                current_node = left_child
            if right_child < size and self.array[right_child] > self.array[current_node]:
                current_node = right_child
            if current_node != i:
                self.array[current_node], self.array[i] = self.array[i], self.array[current_node]
                # 调整后，叶子节点还有子节点，并且不满足大顶堆，又需要对该节点进行调整
                self.adjust_heap(current_node, size)

    def build_heap(self):
        # 父节点是[i-1] / 2
        # 最后一个元素的父节点就是int(size/2)
        # 从下面的父节点开始调整
        for i in range(0, int(len(self.array) / 2))[::-1]:
            self.adjust_heap(i, len(self.array))

    def sort(self):
        """
        堆排序的思想：先调整成大顶堆，1、先从最后一个叶子节点的父节点进行调整，然后在依次进行调整
        2、如果调整后的子节点还有子节点并且不满足大顶堆，那么就采用递归一直调整下去，一直到节点是叶子节点
        调整成大顶堆后，将最后一个元素与堆顶进行交换，然后在进行堆的调整，直到排序完成
        """
        self.build_heap()
        for i in range(0, len(self.array))[::-1]:
            # 调整成大顶堆后，将最后一个元素与堆顶元素进行交换
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.adjust_heap(0, i)

if __name__ == '__main__':
    heap = Heap([6, 1, 2, 7, 9, 3, 4, 5, 10, 8])
    heap.sort()
    print(heap.array)
