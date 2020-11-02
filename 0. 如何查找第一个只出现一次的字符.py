class Solution:
    def findFirstChar(str):
        dic = {}
        for c in str:
            dic[c] = 1 if c not in dic else dic[c] + 1

        for i, c in enumerate(str):
            if dic[c] == 1:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.findFirstChar("abca"))
