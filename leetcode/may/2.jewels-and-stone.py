class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
      mapCh = {}
      for ch in J:
        mapCh[ch] = 1
      count = 0
      for ch in S:
        if ch in mapCh:
          count += 1
      return count