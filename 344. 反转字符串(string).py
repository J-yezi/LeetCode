class Solution(object):
    def reverseString(self, str):
        return ("" if len(str) == 1 else self.reverseString(str[1:])) + str[0]


if __name__ == "__main__":
    s = Solution()
    print(s.reverseString('hello'))
