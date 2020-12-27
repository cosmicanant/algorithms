class Solution:
  def firstUniqChar(self, s: str) -> int:
    mapFirstIndex = {}
    nonRepeating = []
    for c in s:
      if c in mapFirstIndex:
        mapFirstIndex[c] = 1 + mapFirstIndex[c]
      else:
        mapFirstIndex[c] = 1
      nonRepeating.append(c)
    res = -1
    for i in range(len(nonRepeating)):
      if mapFirstIndex[nonRepeating[i]] == 1:
        return i
    return res

"""
better approach:
fc = len(s)
        for c in string.ascii_lowercase:
            left = s.find(c)
            if left != -1 and left == s.rfind(c):
                fc = min(left, fc)
        return fc if fc != len(s) else -1
"""