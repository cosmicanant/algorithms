#Search in Rotated Sorted Array
import math
from typing import List

class Solution:

  def findFaultySubArr(self, nums, start, mid, end):
    if(nums[start] > nums[mid]):
      return [start, mid]
    if(nums[mid] > nums[end]):
      return [mid, end]
    return []
  
  def bs(self, nums, start, end, item):
    mid = math.floor((start + end)*0.5)
    idx = -1
    if item == nums[start]:
      idx = start
    elif item == nums[end]:
      idx = end
    elif item == nums[mid]:
      idx = mid
    elif start == end or start > end or end - start == 1:
      idx = -1
    else:
      faultArr = self.findFaultySubArr(nums, start, mid, end)
      if len(faultArr) > 0:
        a, b = faultArr
        if mid == b: # left faulty
          if nums[mid+1] <= item <= nums[end]:
            idx = self.bs(nums, mid+1, end, item)
          else:
            idx = self.bs(nums, start, mid, item)
        elif mid == a: # right faulty
          if nums[start] <= item <= nums[mid]:
            idx = self.bs(nums, start, mid, item)
          else:
            idx = self.bs(nums, mid+1, end, item)
      else:
        if nums[start] <= item <= nums[mid]:
          idx = self.bs(nums, start, mid, item)
        else:
          idx = self.bs(nums, mid+1, end, item)
    return idx

  def search(self, nums: List[int], target: int) -> int:
    if len(nums) == 0:
      return -1
    idx = self.bs(nums, 0, len(nums)-1, target)  
    return idx  

if __name__ == "__main__":
    sol = Solution()
    res =  sol.search([4,5,6,7,8,1,2,3], 2)
    print(res)

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
'''