from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
      mid = left + (right - left) // 2
      if target == nums[mid]:
        return mid
      if target > nums[mid]:
        left = mid + 1
      else:
        right = mid - 1
    return left if left > right else right

if __name__ == "__main__":
  arr = [ 1, 3, 5, 6]
  target = 4
  sol = Solution()
  print(sol.searchInsert(arr, target))