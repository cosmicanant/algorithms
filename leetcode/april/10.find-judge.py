from typing import List

class Solution:
  def findJudge(self, N: int, trust: List[List[int]]) -> int:
    res = -1
    if N == 1 and len(trust) == 0:
      return 1
    mapPersons = {}
    for [a, b] in trust:
      if a in mapPersons:
        mapPersons[a]["judge"] = False
      else:
        mapPersons[a] = {
          "ct": 0,
          "judge": False
        }
      if b in mapPersons:
        mapPersons[b]["ct"] = mapPersons[b]["ct"] + 1
      else:
        mapPersons[b] = {"ct" : 1, "judge": True}
    for k in mapPersons:
      if mapPersons[k]["ct"] == N-1 and mapPersons[k]["judge"]:
        return k
    return -1

if __name__ == "__main__":
  sol = Solution()
  print(
    sol.findJudge(
      2, [[1,2],[2,1]]
    )
  )

"""
trusters = {x[0] for x in trust}
        trusted_by = 0
        candidate = -1
        for i in range(1, N+1):
            if i not in trusters:
                candidate = i
        
        for a, b in trust:
            if b == candidate:
                trusted_by += 1
        
        if trusted_by != N - 1:
            candidate = -1
            
        return candidate
"""