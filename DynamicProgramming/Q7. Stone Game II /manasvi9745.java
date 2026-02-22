class Solution {
    
    private int[][] dp;
    private int[] suffixSum;
    private int n;
    
    public int stoneGameII(int[] piles) {
        
        n = piles.length;
        dp = new int[n][n + 1];
        suffixSum = new int[n];
        
        // Build suffix sum
        suffixSum[n - 1] = piles[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] = piles[i] + suffixSum[i + 1];
        }
        
        return dfs(0, 1);
    }
    
    private int dfs(int i, int M) {
        
        if (i >= n) return 0;
        
        // If we can take all remaining piles
        if (2 * M >= n - i) {
            return suffixSum[i];
        }
        
        if (dp[i][M] != 0) {
            return dp[i][M];
        }
        
        int minOpponent = Integer.MAX_VALUE;
        
        for (int X = 1; X <= 2 * M; X++) {
            int opponent = dfs(i + X, Math.max(M, X));
            minOpponent = Math.min(minOpponent, opponent);
        }
        
        dp[i][M] = suffixSum[i] - minOpponent;
        return dp[i][M];
    }
}
