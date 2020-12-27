from typing import List

class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    mapP = {}
    for ch in p:
      if ch in mapP:
        mapP[ch] += 1
      else:
        mapP[ch] = 1
    res = []
    searchInProgress = None
    chToBeProcessed  = None
    for i in range(len(s)):
      ch = s[i]
      if searchInProgress:
        if ch in chToBeProcessed:
          chToBeProcessed[ch] -= 1
          if chToBeProcessed[ch] == 0:
            del chToBeProcessed[ch]
        elif ch in mapP:
          j = startIndex
          while j < i:
            if s[j] == ch:
              startIndex = j+1
              break
            if s[j] in chToBeProcessed:
              chToBeProcessed[s[j]] += 1
            else:
              chToBeProcessed[s[j]] = 1
            j += 1
        else:
          searchInProgress = False
      elif ch in mapP:
        searchInProgress = True
        chToBeProcessed = mapP.copy()
        startIndex = i
        chToBeProcessed[ch] -= 1
        if chToBeProcessed[ch] == 0:
          del chToBeProcessed[ch]
      if searchInProgress and len(chToBeProcessed.keys()) == 0:
        res.append(startIndex)
        chToBeProcessed[s[startIndex]] = 1
        startIndex += 1
    return res


if __name__ == "__main__":
  print(Solution()
    .findAnagrams(
      'cbaebabacdcbac', 'abc'
    )
  )