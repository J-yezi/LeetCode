'''
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。

示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
'''


class Solution(object):
    def build(self, str):
        s, s1, sr = len(str) - 1, 0, ''
        while s >= 0:
            if str[s] == '#':
                s -= 1
                s1 += 1
            else:
                if s1 == 0:
                    sr += str[s]
                else:
                    s1 -= 1
                s -= 1
        return sr

    def backspaceCompare(self, S, T):
        return self.build(S) == self.build(T)


if __name__ == "__main__":
    s = Solution()
    print(s.backspaceCompare('a#c', 'b'))
