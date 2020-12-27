
class Solution:

  def getAllNeighbours(self, rowLen, colLen, i, j):
    a1 = [-1, -1, -1, 0, 0, 1, 1, 1]
    a2 = [-1, 0, 1, -1, 1, -1, 0, 1]
    res = []
    for k in range(8):
      newI = i + a1[k]
      newJ = j + a2[k]
      if newI >= 0 and newI < rowLen and newJ >= 0 and newJ < colLen:
        res.append([newI, newJ])
    return res

  def numIslands(self, grid: [[str]]) -> int:
    rowLen = len(grid)
    if rowLen == 0:
      return 0
    colLen = len(grid[0])
    visited = [[False for j in range(colLen)] for i in range(rowLen)]
    stack = [[0,0]]
    count = 0
    while len(stack) > 0:
      idx = stack.pop()
      i = idx[0]
      j = idx[1]
      visited[i][j] = True
      neighbours = self.getAllNeighbours(rowLen, colLen, i, j)
      shouldIncreaseCount = True
      for neighbour in neighbours:
        m = neighbour[0]
        n = neighbour[1]
        if visited[m][n] == False:
          stack.append([m, n])
        elif grid[m][n] == '1':
          shouldIncreaseCount = False
      if shouldIncreaseCount and grid[i][j] == '1':
        count = count + 1
    return count

if __name__ == "__main__":
    sol = Solution()
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    # grid = [["1","0","1","1","0","1","1"]];
    print(sol.numIslands(grid))
  