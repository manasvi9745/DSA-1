#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        
        if (nums.empty()) return 0;
        
        int maxVal = *max_element(nums.begin(), nums.end());
        
        // Step 1: Build points array
        vector<int> points(maxVal + 1, 0);
        for (int num : nums) {
            points[num] += num;
        }
        
        // Step 2: House Robber DP
        int prev2 = 0;          // dp[i-2]
        int prev1 = points[1];  // dp[i-1]
        
        for (int i = 2; i <= maxVal; i++) {
            int current = max(prev1, prev2 + points[i]);
            prev2 = prev1;
            prev1 = current;
        }
        
        return prev1;
    }
};
