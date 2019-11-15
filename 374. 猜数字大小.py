#coding=utf-8

'''
我们正在玩一个猜数字游戏。 游戏规则如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
每次你猜错了，我会告诉你这个数字是大了还是小了。
你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
'''

def guess(i):
    return -1

class Solution:
    def guessNumber(self, n):
        low = 1
        high = n
        while low <= high:
            mid = (high - low) / 2 + low
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                low = mid + 1
            else:
                high = mid - 1
        return None

if __name__ == "__main__":
    s = Solution()
