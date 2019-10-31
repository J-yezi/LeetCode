#coding=utf-8

class Solution:
    # 暴力法
    # def maxProfit(self, prices):
    #     dis = 0
    #     for i in range(len(prices)):
    #         for j in range(i + 1, len(prices)):
    #             dis = max(dis, prices[j] - prices[i])
    #     return dis

    def maxProfit(self, prices):
        dis = 0
        trough = float("inf")
        for i in prices:
            if i < trough:
                trough = i
            else:
                dis = max(dis, i - trough)
        return dis

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))