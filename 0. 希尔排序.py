class Shell:
    def __init__(self, array):
        self.array = array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def sort(self):
        """
        希尔排序的原理例如先划分间隔3来进行排序，然后可以用2进行间隔排序，最后肯定是变成间隔为1，
        前面就基本排序，后面第二次间隔排序和后面间隔排序，需要进行交换的数据就会变少，最后间隔为1，
        进行统一的排序
        """
        increment = len(self.array)
        length = increment
        while increment > 1:
            # 每次减小增量，直到increment = 1
            increment = int(increment / 3) + 1
            # 插入排序
            for i in range(increment, length):
                j = i - increment
                while self.array[j] > self.array[j + increment] and j >= 0:
                    self.swap(j, j + increment)
                    j -= increment


if __name__ == '__main__':
    shell = Shell([4, 1, 7, 3, 8, 5, 9, 2, 6, 0, 123, 22])
    shell.sort()
    print(shell.array)
