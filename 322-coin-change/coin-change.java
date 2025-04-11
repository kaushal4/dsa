class Solution {
    
    public int recur(int [] coins, int sum, int[] dp){
        int ans = Integer.MAX_VALUE;
        if(sum == 0)
        {
            return 0;
        }
        if(dp[sum] != -1) {
            return dp[sum];
        }
        for(int i = 0; i < coins.length; i++)
        {
            if(coins[i] > sum)
            {
                continue;
            }
            ans = Math.min(recur(coins, sum - coins[i], dp), ans);
        }
        dp[sum] = ans == Integer.MAX_VALUE? Integer.MAX_VALUE: ans+1;
        return dp[sum];
    }

    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount+1];
        Arrays.fill(dp, -1);
        int res = recur(coins, amount, dp);
        return res == Integer.MAX_VALUE? -1 : res;
    }
}