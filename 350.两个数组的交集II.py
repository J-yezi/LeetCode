#coding=utf-8

class Solution:
    # def intersect(self, nums1, nums2):
    #     dic = {}
    #     for i in nums1:
    #         try:
    #             dic[i] += 1
    #         except:
    #             dic[i] = 1

    #     arr = []
    #     for i in nums2:
    #         try:
    #             if dic[i] > 0:
    #                 dic[i] -= 1
    #                 arr.append(i)
    #         except: pass
    #     return arr

    # 双指针方法 
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1 = 0
        p2 = 0

        arr = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                arr.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.intersect([4,9,5], [9,4,9,8,4]))