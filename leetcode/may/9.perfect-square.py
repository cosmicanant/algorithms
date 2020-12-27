class Solution:
  def bs(self, start, end, num):
    if start <= end:
      mid = start + (end - start)//2        
      if mid * mid == num:
        return True
      elif mid == start and start == end:
        return False
      elif mid*mid > num:
        return self.bs(start, mid-1, num)
      else:
        return self.bs(mid+1, end, num)      
    return False
    
  def isPerfectSquare(self, num: int) -> bool:
    return self.bs(0, num, num)

if __name__ == "__main__":
  print(Solution().isPerfectSquare(145))