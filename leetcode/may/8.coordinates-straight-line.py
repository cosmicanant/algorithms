class Solution:
  def getDiff(self, x, y):
    return [
      abs(x[0] - y[0]),
      abs(x[1] - y[1])
    ]
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    if len(coordinates) < 2:
      return False
    if len(coordinates) == 2:
        return True
    xFactor, yFactor = self.getDiff(coordinates[0], coordinates[1])
    prev = coordinates[1]
    for i in range(2, len(coordinates)):
      curr = coordinates[i]
      x, y = self.getDiff(prev, curr)
      if xFactor == 0:
        if x != 0:
          return False
      elif yFactor == 0:
        if y != 0:
          return False
      else:
        if xFactor/yFactor != x/y:
          return False
      prev = curr
    return True