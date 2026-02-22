class Solution {
    public int knightDialer(int n) {
        
        int MOD = 1_000_000_007;
        
        long[] dp = new long[10];
        
        // Base case: n = 1
        for (int i = 0; i < 10; i++) {
            dp[i] = 1;
        }
        
        int[][] moves = {
            {4,6},     // 0
            {6,8},     // 1
            {7,9},     // 2
            {4,8},     // 3
            {0,3,9},   // 4
            {},        // 5
            {0,1,7},   // 6
            {2,6},     // 7
            {1,3},     // 8
            {2,4}      // 9
        };
        
        for (int step = 2; step <= n; step++) {
            long[] newDp = new long[10];
            
            for (int digit = 0; digit < 10; digit++) {
                for (int next : moves[digit]) {
                    newDp[next] = (newDp[next] + dp[digit]) % MOD;
                }
            }
            
            dp = newDp;
        }
        
        long result = 0;
        for (int i = 0; i < 10; i++) {
            result = (result + dp[i]) % MOD;
        }
        
        return (int) result;
    }
}
