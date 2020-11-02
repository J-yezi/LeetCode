class Bubble:
    def __init__(self, array=None):
        self.array = array

    def swap(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def sort(self):
        """
        冒泡排序算法，时间复杂度O(n^2)，稳定，使用场景：n较小时
        """
        for i in range(len(self.array)):
            for j in range(i + 1, len(self.array)):
                if self.array[i] > self.array[j]:
                    self.swap(i, j)


if __name__ == '__main__':
    bubble = Bubble([4, 1, 7, 3, 8, 5, 9, 2, 6])
    bubble.sort()
    print(bubble.array)
