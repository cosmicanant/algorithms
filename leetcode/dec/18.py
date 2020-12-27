from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        min1 = min(nums[0], nums[1], nums[2])
        min1 = 0
        if nums[1] == min1:
            min1 = 1
        elif nums[2] == min1:
            min1 = 2
        min2 = None
        min3 = None
        for i in range(min1+1, len(nums)):
            if nums[i] <= nums[min1]:
                if nums[i] == nums[min1]:
                    continue
                min1 = i
                min2 = None
                min3 = None
            elif min2 is None:
                min2 = i
                min3 = None
            elif min3 is None:
                if nums[i] == nums[min2]:
                    continue
                if nums[i] > nums[min2]:
                    min3 = i
                else:
                    min2 = i
                    continue
        return min3 is not None
if __name__ == "__main__":
    print(Solution().increasingTriplet([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,3]))