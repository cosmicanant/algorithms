from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
      x = [i for i in range(len(s))]
      if len(s) == 0 or len(shift) == 0:
        return s
      for row in shift:
        if row[1] == 0:
          continue         
        if row[0] == 0:
          x = x[row[1]:] + x[0:row[1]]
        else:
          x =  x[-(row[1]):] + x[0: len(s) - row[1]]
      res = ''
      for i in x:
        res = res + s[i]
      return res

if __name__ == "__main__":
    sol = Solution()
    res =  sol.stringShift("abc",[[0,1],[1,2]])
    print(res)

"""
alternative sol with O(1) space complexity
class Solution:
    def stringRotation(self, s: str, rotation: List[List[int]]) -> str:
        left = 0
        for d, a in rotation:
            if d:
                left -= a
            else:
                left += a
        left %= len(s)
        return s[left:] + s[:left]
"""
