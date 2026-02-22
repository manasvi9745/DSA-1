class Solution {

    private int n;
    private int[][][] dp;

    public int cherryPickup(int[][] grid) {
        n = grid.length;
        dp = new int[n][n][n];

        // Initialize DP with Integer.MIN_VALUE
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    dp[i][j][k] = Integer.MIN_VALUE;
                }
            }
        }

        int result = solve(0, 0, 0, grid);
        return Math.max(0, result);
    }

    private int solve(int r1, int c1, int r2, int[][] grid) {
        int c2 = r1 + c1 - r2;

        // Out of bounds or thorn
        if (r1 >= n || c1 >= n || r2 >= n || c2 >= n ||
            grid[r1][c1] == -1 || grid[r2][c2] == -1) {
            return -1000000;  // large negative for invalid
        }

        // Reached bottom-right
        if (r1 == n - 1 && c1 == n - 1) {
            return grid[r1][c1];
        }

        if (dp[r1][c1][r2] != Integer.MIN_VALUE) {
            return dp[r1][c1][r2];
        }

        int cherries = grid[r1][c1];

        // Avoid double count
        if (r1 != r2) {
            cherries += grid[r2][c2];
        }

        int best = Math.max(
                Math.max(
                        solve(r1 + 1, c1, r2 + 1, grid), // down, down
                        solve(r1 + 1, c1, r2, grid)      // down, right
                ),
                Math.max(
                        solve(r1, c1 + 1, r2 + 1, grid), // right, down
                        solve(r1, c1 + 1, r2, grid)      // right, right
                )
        );

        cherries += best;
        dp[r1][c1][r2] = cherries;

        return cherries;
    }
}
