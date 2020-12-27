from typing import List
# https://leetcode.com/problems/valid-mountain-array/
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)
        if l < 3:
            return False
        found = False
        for i in range(1, l):
            if found:
                if arr[i] < arr[i-1]:
                    continue;
                else:
                    found = False
                    break;
            else:
                if arr[i] > arr[i-1]:
                    continue
                elif arr[i] < arr[i-1] and i > 1:
                    found = True
                    continue
                else:
                    break
        return found
    
if __name__ == "__main__":
    print(Solution().validMountainArray([9, 8, 7,6,5,4,3,2,1,0]))