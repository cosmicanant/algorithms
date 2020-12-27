
from typing import List

class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    # 0 -1 -2 -1 0
    #-1 0  1 2  3
    mapSum = {0: -1}
    sm = 0
    maxLength = 0
    for i in range(len(nums)):
      num = nums[i]
      if num == 0:
        sm -= 1
      else:
        sm += 1
      if sm in mapSum:
        maxLength = max(maxLength, i - mapSum[sm])
      else:
        mapSum[sm] = i    
    return maxLength
  
if __name__ == "__main__":
  sol = Solution()
  print(
    sol.findMaxLength(
      [0, 0, 1, 1]
    )
  )
"""
        numLen = len(nums)
        if numLen == 0 or numLen == 1:
          return 0
        ob = {0 : 0}
        count = 0
        maxRes = 0
        for i in range(1, numLen+1):
          count = count + ( -1 if nums[i-1] == 0 else 1)
          if count in ob:
            maxRes = max(maxRes, i - ob[count])
          else:
            ob[count] = i
        return maxRes
"""
