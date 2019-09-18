class Solution:
    def combinationSum(self, candidates, target):
        self.getcombinationSum(candidates, [], 0, target)
        pass

    def getcombinationSum(self, candidates, prefix, curr, target):
        for i in candidates:
            if curr + i == target:
                prefix.append(i)
                return
            elif curr + i > target:
                return
            else:
                prefix.append(i)
                curr = curr + i
                self.getcombinationSum(candidates, prefix, curr, target)

if __name__ == '__main__':
    s = Solution()
    print