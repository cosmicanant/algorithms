# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        runningIndex = 2
        currCount = 1
        l = len(nums)
        # [0,0,1,1,1,1,2,3,3]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                currCount += 1 
            else:
                currCount = 1
            if currCount <= 2 and runningIndex <= i:
                nums[runningIndex] = nums[i]
                runningIndex += 1
        return nums

if __name__ == "__main__":
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 3]))
