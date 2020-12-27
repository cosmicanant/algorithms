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
};

var res = maxSubArray([1, 2, -2, 1]);
console.log(res);

