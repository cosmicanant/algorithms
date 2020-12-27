from typing import List
class Solution:
  
  def dfs(self, node, bag, visited):
    if visited[node] == 'visiting':
      return False
    visited[node] = 'visiting'
    neighbours = bag[node]
    for k in neighbours:
      if visited[k] != 'visited':
        tmp = self.dfs(k, bag, visited)
        if tmp == False:
          return tmp
    visited[node] = 'visited'
    return True
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    bag = [[] for _ in range(numCourses)]
    for j, i in prerequisites:
      bag[i].append(j)
    visited = ['unvisited' for _ in range(numCourses)]
    for i in range(numCourses):
      if visited[i] == 'unvisited':
        tmp = self.dfs(i, bag, visited)
        if tmp == False:
          return tmp
    return True
  
if __name__ == "__main__":
  sol = Solution()
  print(
    sol.canFinish( 3 ,[[1, 0],  [2, 1]])
  )
  