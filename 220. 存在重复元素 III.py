"""
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，
且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。
"""


class Solution(object):
    # 两次for循环，会超时
    def containsNearbyAlmostDuplicate1(self, nums, k, t):
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False

    """
    桶排序
    1、使用哈希表来模拟桶，key就是桶号，value就是数字本身
    2、定义桶的大小是t+1, nums[i]//(t+1)决定放入几号桶，
        这样在一个桶里面的任意两个的绝对值差值都<=t
    3、例如t=3, nums=[0 ,5, 1, 9, 3,4],那么0号桶就有[0,1,3],1号桶就有[4,5],2号桶就有[9]
    4、例如t=2，那么nums[i]=9的时候，就应该移除bucket.pop(nums[i - k] // (t + 1))
    5、如果碰到元素在同一个桶里面，那么就直接返回true
    6、可以和桶序号相邻的桶进行比较，例如当前桶序号是n，那么相邻的就是n-1或者n+1
        不会出现去找n-2这样的情况，因为n-2的话，表示两个桶的数组至少相差了t+1
    """
    def containsNearbyAlmostDuplicate2(self, nums, k, t):
        bucket = dict()
        if t < 0:
            return False

        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k:
                bucket.pop(nums[i - k] // (t + 1))
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyAlmostDuplicate2([1, 5, 12, 1, 5, 9], 2, 3))
