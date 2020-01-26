class Merge:
    def __init__(self, array):
        self.array = array

    """
    归并排序的思路：将整个数组分成左右两个，然后在继续拆分，直到数组只有一个，那么这个
    数组就可以看成是有序的数组，这个也是递归结束的条件，然后再将左右两个数组合并
    """
    def merge_sort(self, seq):
        if len(seq) <= 1:
            return seq
        # 将列表分成更小的两个列表
        mid = int(len(seq) / 2)
        # 分别对左右两个列表进行处理，分别返回两个排序好的列表
        left = self.merge_sort(seq[:mid])
        right = self.merge_sort(seq[mid:])
        # 对排序好的两个列表合并，产生一个新的排序好的列表
        return self.merge(left, right)

    """
    left和right都是已经排好序的两个列表，将这两个列表合并
    """
    def merge(self, left, right):
        result = []  # 新的已排序好的列表
        i = 0  # 下标
        j = 0
        # 对两个列表中的元素 两两对比。
        # 将最小的元素，放到result中，并对当前列表下标加1
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

    def sort(self):
        self.array = self.merge_sort(self.array)

if __name__ == '__main__':
    merge = Merge([6, 1, 2, 7, 9, 3, 4, 5, 10, 8])
    merge.sort()
    print(merge.array)