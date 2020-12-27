class Solution:
  def dfs(self, i, colorCode, bags, colors):
    colors[i] = colorCode
    for j in bags[i]:
      if j in colors and colors[j] == colorCode:
        return False
      elif j not in colors:
        tmp = self.dfs(j, -colorCode, bags, colors)
        if not tmp:
          return False
    return True
  def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
    bag = [[] for _ in range(N+1)]
    for i, j in dislikes:
      bag[i].append(j)
      bag[j].append(i)
    colors = {}
    for i, j in dislikes:
      if i not in colors and not(self.dfs(i, 1, bag, colors)):
        return False
    return True
        