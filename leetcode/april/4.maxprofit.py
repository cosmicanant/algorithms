import sys
class Solution:
    def maxProfit(self, prices: [int]) -> int:
      days = len(prices)
      if days == 0:
        return 0;
      if days == 1:
        return 0;
      if days == 2:
        return 0 if prices[1] <= prices[0] else prices[1] - prices[0]
      dp = [0, 0]
      dp[0] = 0;
      dp[1] = 0 if prices[1] <= prices[0] else prices[1] - prices[0]
      
      for i in range(2, days):
        dayProfit = max([dp[i-1], dp[i-1] - prices[i-1] + prices[i], prices[i] - prices[i-1]])
        dp.append(dayProfit);
      
      return max(dp)

if __name__ == "__main__":
    sol = Solution()
    arr = [7,6,4,3,1]
    profit = sol.maxProfit(arr);
    print(arr)
    print(profit)
'''
dp [0] = 0
dp[1] = 1
dp[2] = 3 - (1 + 2) = 0
dp[3] = 2 - 3 + 

'''
