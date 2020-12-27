from typing import List
import math


class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        mapSum = {0: 1}
        count, currSum = [0, 0]
        for i in range(len(nums)):
            currSum += nums[i]
            if (currSum - k) in mapSum:
                count += mapSum[currSum - k]
            mapSum[currSum] = (1 + mapSum[currSum]) if currSum in mapSum else 1
        return count

if __name__ == "__main__":
    sol = Solution()
    arr = [0, 0, 2, 0]
    # -3, 3
    count = sol.subarraySum(arr, 2)
    print(count)
""" 
public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
} """
