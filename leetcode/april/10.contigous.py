class Solution:
    def findMaxLength(self, nums: [int]) -> int:
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

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaxLength([0,1, 1]))