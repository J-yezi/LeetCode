#coding=utf-8

'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题
'''

class Solution:
    # 递归
    # def reverseString(self, s):
    #     self._reverseString(s, 0)
    #     return s

    # def _reverseString(self, s, index):
    #     if index >= len(s) - index - 1:
    #         return
    #     else:
    #         s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
    #         self._reverseString(s, index + 1)

    # 双指针
    def reverseString(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))