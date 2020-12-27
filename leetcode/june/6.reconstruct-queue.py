from typing import List
class Solution:
  def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    people.sort(key = lambda x: x[0])
    arr = [None] * len(people)
    for el, k in people:
      el, k = people.pop(0)
      arr.insert(0, [el, k])
      if k > 0:
        while k > 0 and len(people) > 0:
          arr.insert(0, people.pop(0))
          k -= 1
    return arr 

if __name__ == "__main__":
  print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

"""
[4, 4], [5,2], [5,0], [6,1], [7,0], [7,1]
[5,0],  [7,0], [5,2], [4,4], [6,1], [7,1]
"""
