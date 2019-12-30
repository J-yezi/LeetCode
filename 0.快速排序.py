class Quick:
    def __init__(self, array):
        self.array = array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def sort(self):
        self.quick_sort(0, len(self.array) - 1)

    def quick_sort(self, left, right):
        """
        快速排序的思想：先设定第一个元素为key，然后进行排序，左边始终小于key，右边一直大于key
        然后采用递归，对key左边和右边的数组分别进行排序
        """
        if left >= right:
            return

        low = left
        high = right
        key = self.array[left]
        # 先从右边进行比较，知道右边的数据小于key，然后进行交换，保证左边的数据始终小于key
        # 然后又从左边比较，直到左边数据大于key，又交换到右边
        while left < right:
            while left < right and self.array[right] > key:
                right -= 1
            self.swap(left, right)
            while left < right and self.array[left] < key:
                left += 1
            self.swap(left, right)

        self.quick_sort(low, left - 1)
        self.quick_sort(right + 1, high) 

if __name__ == '__main__':
    quick = Quick([6, 1, 2, 7, 9, 3, 4, 5, 10, 8])
    quick.sort()
    print(quick.array)