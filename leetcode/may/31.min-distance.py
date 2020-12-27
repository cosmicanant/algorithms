class Solution:
  def minDistance(self, word1: str, word2: str) -> int:
    m = len(word1) + 1
    n = len(word2) + 1
    dp = [[[] for _ in range(n)] for _ in range(m)]
    for i in range(m):
      if i == 0:
        continue
      for j in range(n):
        if j == 0:
          continue
        if word1[i-1] == word2[j-1]:
          dp[i][j] = dp[i-1][j-1][0:] + [[i-1, j-1]]
        else:
          dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
    arr = dp[m-1][n-1]
    # [1, 0], [2, 1], [3, 2]
    if len(arr) > 0:
      sol = 0
      t1 = -1
      t2 = -1
      for i, j in arr:
        sol += (i - (t1+1)) if (i - (t1 +1)) > (j - (t2+1)) else (j - (t2+1))
        t1 = i
        t2 = j
      sol += (n - 2) - t2
      return sol
    else:
      return m-1 if m > n else n -1
  
if __name__ == "__main__":
  sol = Solution()
  print(
    sol.minDistance( 'intention', 'execution')
  )
            
# inten
# execu