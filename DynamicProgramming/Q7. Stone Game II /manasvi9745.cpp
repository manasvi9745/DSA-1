#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int n;
    vector<int> suffixSum;
    vector<vector<int>> dp;
    
    int solve(int i, int M, vector<int>& piles) {
        
        if (i >= n) return 0;
        
        // If current player can take all remaining piles
        if (2 * M >= n - i) {
            return suffixSum[i];
        }
        
        if (dp[i][M] != -1) {
            return dp[i][M];
        }
        
        int minOpponent = 1e9;
        
        for (int X = 1; X <= 2 * M; X++) {
            int opponent = solve(i + X, max(M, X), piles);
            minOpponent = min(minOpponent, opponent);
        }
        
        dp[i][M] = suffixSum[i] - minOpponent;
        return dp[i][M];
    }
    
    int stoneGameII(vector<int>& piles) {
        
        n = piles.size();
        suffixSum.resize(n);
        
        // Build suffix sums
        suffixSum[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] = piles[i] + suffixSum[i + 1];
        }
        
        dp.assign(n, vector<int>(n + 1, -1));
        
        return solve(0, 1, piles);
    }
};
