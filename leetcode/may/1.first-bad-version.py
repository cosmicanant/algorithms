# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# sample isBadVersion given below
def isBadVersion(version):
  return True

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        
        while low < high:
            mid = low + (high-low) // 2
            if isBadVersion(mid) is True:
                high = mid
            elif isBadVersion(mid) is False:
                low = mid+1
        return low