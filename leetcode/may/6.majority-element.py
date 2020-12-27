import math

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    countMap = {}
    for num in nums:
      if num in countMap:
        countMap[num] = countMap[num] + 1
      else:
        countMap[num] = 1
    ct = math.ceil(len(nums) / 2)  
    for key in countMap:
      if countMap[key] >= ct:
        return key
          