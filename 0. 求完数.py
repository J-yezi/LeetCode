#coding=utf-8

class Solution(object):
  def resolve(self):
    result = []
    for i in range(1, 1001):
      sum = i
      for j in range(1, i):
        if i % j == 0:
          sum -= j
      if sum == 0:
        result.append(i)
    return result

if __name__ == "__main__":
  s = Solution()
  print(s.resolve())
  pass
