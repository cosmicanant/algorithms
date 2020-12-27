"""
kadane algo: keep track of max sum of contiguous elements
maxSumOfCurrentContagiousElements = max(lastContigousSum + currElement, currElement)
NOTE: for each iteration level, we must need to include the curr element in the  contagious sum
lastElement ( positive) and currElement ( Positive) : simply add the last contigious sum + currElement to keep the max contagious sum ( including the currEl)
lastElement ( positive) and currElement ( negative) : simply add the last contigious sum + currElement to keep the max contagious sum ( including the currEl)
lastElement(negative) and currElement( positive):  simply pick the positive only( current only) to keep the max contagious sum( discard last negative)
lastElement(negative) and currElement( negative):  simply pick the curr element and discard the last one ( as last negative elem will only decrease  the sum)

now answer  will be max of all the contagious sum for each iteration, use a variable to keep comparing the max with previous max

example:
arr = [1 -3 -4 5 2]

1. first iteration: // init step
currContagiouMaxSum = 1
maxContagiousSum = 1

2. ( notice how the cuurrent element takes part in the sum)
currContagiouMaxSum = max(currContagiouMaxSum + currEl, currElement) = max(1 - 3, -3) = -2
maxContagiousSum = max(maxContagiousSum, currContagiouMaxSum) = max(1, -2) = 1

3. ( notice how the last negative element discarded ie: -3, it was done to keep the  contagious sum maximum)
currContagiouMaxSum = max(currContagiouMaxSum + currEl, currElement) = max(-2 - 4, -4) = -4
maxContagiousSum = max(maxContagiousSum, currContagiouMaxSum) = max(1, -4) = 1

4. 
currContagiouMaxSum = max(currContagiouMaxSum + currEl, currElement) = max(- 4 + 5, 5) = 5
maxContagiousSum = max(maxContagiousSum, currContagiouMaxSum) = max(1, 5) = 5

5. 
currContagiouMaxSum = max(currContagiouMaxSum + currEl, currElement) = max(5 + 2, 2) = 7
maxContagiousSum = max(maxContagiousSum, currContagiouMaxSum) = max(5, 7) = 7

no more iteration is remaining, so answer = maxContagiousSum

Notes:  In case of circular Array, find the min sum, totalSum, and maxSum,

maxSum for contagious array will be: 
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum

"""

class Solution:
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    currMax, currMin, total = A[0], A[0], A[0]
    maxSum, minSum = A[0], A[0]
    # [1,-2,3,-2]

    # kadane algo for finding max
    # traverse array  and divide problem into two sub problems
    # keep track the contagious sum when the contagious no are positive : max(currMax + A[i], A[i])
    # keep track the min when contagiouus elements are nagative: max(currMax + A[i], A[i]) as the min will costitue the highest sum
    # also, keep track 
    for i in range(1, len(A)):
      total = total + A[i]
      currMax = max(currMax + A[i], A[i])
      currMin = min(currMin + A[i], A[i])
      maxSum = max(maxSum, currMax)
      minSum = min(minSum, currMin)
    return max(maxSum, total - minSum) if maxSum > 0 else maxSum
    
"""
var maxSubArray = function(nums) {
  let dp = [];
  dp[0] = nums[0];
  var sum = nums[0];
  for(let i = 1;i < nums.length;i++) {
    dp[i] = Math.max(dp[i - 1] + nums[i], nums[i]);
    sum = Math.max(dp[i], sum)
  }
  console.log(dp);
  return sum;

  [1,-2,3,-2]
  1, 
  max(-1, -2), -1
  max( currMax, max)

  
};
"""