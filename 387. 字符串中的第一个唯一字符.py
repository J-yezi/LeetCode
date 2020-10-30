class Solution:
    def firstUniqChar(self, s):
        dic = {}
        for i in range(len(s)):
            if s[i] in dic.keys():
                (index, count) = dic[s[i]]
                count += 1
                dic[s[i]] = (index, count)
            else:
                dic[s[i]] = (i, 1)

        i = -1
        for key in dic.keys():
            (index, count) = dic[key]
            if count == 1:
                if i == -1:
                    i = index
                else:
                    i = min(i, index)
        return i


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar('loveleetcode'))
