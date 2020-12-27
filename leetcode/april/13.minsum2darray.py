from typing import List
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      rowLen = len(grid)
      if rowLen == 0:
        return 0
      colLen = len(grid[0])
      sol = [[math.inf]*(colLen+1) for j in range(rowLen +1)]

      for i in range(1, rowLen+1):
        for j in range(1, colLen+1):
          left = sol[i][j-1]
          top = sol[i-1][j]
          if left == math.inf and top == math.inf:
            sol[i][j] = grid[i-1][j-1]
          elif left == math.inf:
            sol[i][j] = top + grid[i-1][j-1]
          elif top == math.inf:
            sol[i][j] = left + grid[i-1][j-1]
          else:
            sol[i][j] = min(left, top) + grid[i-1][j-1]
      return sol[rowLen][colLen]


if __name__ == "__main__":
    sol = Solution()
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    # grid = [["1","0","1","1","0","1","1"]];
    print(sol.minPathSum(grid))
  