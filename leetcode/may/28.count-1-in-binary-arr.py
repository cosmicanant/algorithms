from typing import List

class Solution:
  def countBits(self, num: int) -> List[int]:
  # 0, 1, 1+0, 1+1, 1 + 0, 1 + 1, 1 + 1, 1 + 2,
    if num == 0:
      return [0]
    arr = [0, 1]
    if num == 1:
      return arr
    power = 1
    while len(arr) <= num:
      ct = 2**power
      for i in range(ct):
        arr.append(1 + arr[i])
        if len(arr) == num + 1:
          break
      power = power + 1
    return arr
# 0,1,1,2,1,2

if __name__ == '__main__':
  sol = Solution()
  k = sol.countBits(7)
  print(k)