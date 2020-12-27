from typing import List

class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    if len(nums) == 0:
      return []
    nums.sort()
    dp = [[nums[i]] for i in range(len(nums))]
    maxLenIndex = 0
    for i in range(1, len(nums)):
      j = i - 1
      while j >= 0:
        if nums[i] % nums[j] == 0:
          tmp = dp[j] + [nums[i]]
          if len(tmp) > len(dp[i]):
            dp[i] = tmp
        j = j - 1
      if len(dp[i]) > len(dp[maxLenIndex]):
        maxLenIndex = i
    return dp[maxLenIndex]

            

if __name__ == "__main__":
  sol = Solution()
  s = sol.largestDivisibleSubset([3, 8, 9, 16, 27, 32])
  print(s)