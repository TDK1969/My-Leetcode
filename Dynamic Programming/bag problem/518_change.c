int change(int amount, int* coins, int coinsSize)
{
    if (amount == 0) {
        return 1;
    }

    int *dp = (int *)malloc(sizeof(int) * (amount + 1));
    memset(dp, 0, sizeof(int) * (amount+ 1));

   dp[0] = 1;

    for (int j = 0; j < coinsSize; j++) {//先枚举硬币
        for (int i = 0; i <= amount; i++) {//再枚举金额
            if ((long long)i + coins[j] <= (long long)amount) {
                    dp[i + coins[j]] += dp[i];
                }
            }
    }
    

    return dp[amount];
}