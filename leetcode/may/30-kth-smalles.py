import random
from typing import List

class Solution:
  def swap(self, arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr
  def partition(self, arr, left, right, pivotIdx):
    self.swap(arr, left, pivotIdx)
    pivotIdx = left
    pivot = arr[pivotIdx]
    firstMax = None
    for i in range(left, right + 1):
      if i == pivotIdx:
        continue
      if self.compare(pivot, arr[i]) > 0:
        if firstMax:
          self.swap(arr, firstMax, i)
          firstMax += 1
      else:
        if firstMax is None:
          firstMax = i
    if firstMax is not None:
      idx = firstMax - 1
      self.swap(arr, pivotIdx, idx)
      return idx
    self.swap(arr, pivotIdx, right)
    return  right
  def quickSort(self, arr, left, right, k):
    pivot = random.choice(range(left, right+1))
    partIndex = self.partition(arr, left, right, pivot)
    if partIndex == k:
      return partIndex
    elif k < partIndex:
      return self.quickSort(arr, left, partIndex-1, k)
    else:
      return self.quickSort(arr, partIndex+1, right, k)
    
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
      kth = self.quickSort(points, 0, len(points)-1, K - 1)
      k = points[kth]
      res = []
      for el in points:
        if self.compare(k, el) >= 0:
          res.append(el)
        if (len(res) == k):
          break
      return res
  def compare(self, x, y):
    return (x[0]**2 + x[1]**2) - (y[0]**2 +y[1]**2)
            
  
if __name__ == "__main__":
  sol = Solution()
  print(
    sol.kClosest( [[4,0],[2,0], [0,0]], 2)
  )
  