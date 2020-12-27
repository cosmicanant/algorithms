class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    maps1 = {}
    for ch in s1:
      if ch in maps1:
        maps1[ch] += 1
      else:
        maps1[ch] = 1
    searchInProgress = None
    chToBeProcessed  = None
    for i in range(len(s2)):
      ch = s2[i]
      if searchInProgress:
        if ch in chToBeProcessed:
          chToBeProcessed[ch] -= 1
          if chToBeProcessed[ch] == 0:
            del chToBeProcessed[ch]
        elif ch in maps1:
          j = startIndex
          while j < i:
            if s2[j] == ch:
              startIndex = j+1
              break
            elif s2[j] in chToBeProcessed:
              chToBeProcessed[s2[j]] += 1
            else:
              chToBeProcessed[s2[j]] = 1
            j += 1
        else:
          searchInProgress = False
      elif ch in maps1:
        searchInProgress = True
        chToBeProcessed = maps1.copy()
        startIndex = i
        chToBeProcessed[ch] -= 1
        if chToBeProcessed[ch] == 0:
          del chToBeProcessed[ch]
      if searchInProgress and len(chToBeProcessed.keys()) == 0:
        return True
    return False

if __name__ == "__main__":
  print(Solution()
    .checkInclusion(
      'adcef', 'dcdaekkacdef'
    )
  )