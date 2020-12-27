from typing import List

class Solution:
  def getKey(self, i, j):
    return str(i) + str(j)

  def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    if len(image) == 0:
      return image
    stack = [[sr, sc]]
    color = image[sr][sc]
    rowLen = len(image)
    colLen = len(image[0])
    processed = {}
    while(len(stack) > 0):
      [i, j] = stack.pop()
      k = self.getKey(i, j)
      if k in processed:
        continue
      image[i][j] = newColor
      processed[k] = 1
      if i - 1 >= 0 and image[i-1][j] == color:
        stack.append([i-1, j])
      if j + 1 < colLen and image[i][j+1] == color:
        stack.append([i, j+1])
      if i + 1 < rowLen and image[i+1][j] == color:
        stack.append([i+1, j])
      if j - 1 >= 0 and image[i][j-1] == color:
        stack.append([i, j-1])
    return image