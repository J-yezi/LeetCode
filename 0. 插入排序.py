class Insert:
    def __init__(self, array):
        self.array = array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def sort(self):
        """
        最好的情况时间复杂度O(n)，最坏的情况时间复杂度是O(n^2)，平均时间复杂度是O(n^2)，空间复杂度是O(1)，使用场景：大部分已经排好序，稳定
        插入排序的原理，将第一个元素看成是有序数组，然后后面的元素一个一个和前面的有序数组进行比较
        将后面的元素逐渐插入到前面的有序数组中
        """
        for i in range(1, len(self.array)):
            j = i - 1
            while self.array[j] > self.array[j + 1] and j >= 0:
                self.swap(j + 1, j)
                j -= 1


if __name__ == '__main__':
    insert = Insert([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    insert.sort()
    print(insert.array)
