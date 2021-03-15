#include <vector>

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            sum += nums[i];
        }
        if (sum < S || (sum + S) % 2 != 0) {
            return 0;
        }
        int target = (S + sum) / 2;
        int dp[target + 1];
        for (int i = 0 ; i < target+1; i++) {
            dp[i] = 0;
        }
        dp[0] = 1;
        for (int i = 0; i < (int)nums.size(); i++) {
            for (int j = target; j >= nums[i]; j--) {
                dp[j] += dp[j - nums[i]];
            }
        }
        return dp[target];
    }
};