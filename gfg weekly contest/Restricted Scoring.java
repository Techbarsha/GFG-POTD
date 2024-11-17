class Solution {
    public static int getCount(int n) {
        // code here
        final int M = 1000000007;
        int[][] dp = new int[n + 1][2];

        dp[0][0] = 1; 
        dp[0][1] = 0;

        for (int i = 1; i <= n; i++) {
            dp[i][0] = dp[i - 1][0];
            if (i >= 2) dp[i][0] = (dp[i][0] + dp[i - 2][0]) % M;
            if (i >= 6) dp[i][0] = (dp[i][0] + dp[i - 6][0]) % M;

            dp[i][0] = (dp[i][0] + dp[i - 1][1]) % M;
            if (i >= 2) dp[i][0] = (dp[i][0] + dp[i - 2][1]) % M;
            if (i >= 6) dp[i][0] = (dp[i][0] + dp[i - 6][1]) % M;

            if (i >= 4) dp[i][1] = dp[i - 4][0];
        }

        return (dp[n][0] + dp[n][1]) % M;
    }
}
