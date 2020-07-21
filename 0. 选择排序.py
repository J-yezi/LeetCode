#coding=utf-8

class Select:
    def __init__(self, array):
        self.array = array

    def sort(self):
		"""
		选择排序的思想：每次循环都找出最小的那个数值，然后交换
		"""
        for i in range(len(self.array)):
            min, index = self.array[i], i
            for j in range(i + 1, len(self.array)):
                if min > self.array[j]:
                    min = self.array[j]
                    index = j
            self.array[i], self.array[index] = self.array[index], self.array[i]

if __name__ == "__main__":
    s = Select([4, 1, 7, 3, 8, 5, 9, 2, 6])
    s.sort()
    print(s.array)