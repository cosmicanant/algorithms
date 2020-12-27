class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    mapCh = {}
    for ch in magazine:
      mapCh[ch] = (mapCh[ch] + 1) if ch in mapCh else 1
    for ch in ransomNote:
      if ch not in mapCh:
        return False
      if mapCh[ch] > 1:
        mapCh[ch] = mapCh[ch] - 1
      else:
        del mapCh[ch]
    return True