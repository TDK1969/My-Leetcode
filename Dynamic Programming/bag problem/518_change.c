int change(int amount, int* coins, int coinsSize)
{
    if (amount == 0) {
        return 1;
    }

    int *dp = (int *)malloc(sizeof(int) * (amount + 1));
    memset(dp, 0, sizeof(int) * (amount+ 1));

   dp[0] = 1;

    for (int j = 0; j < coinsSize; j++) {//��ö��Ӳ��
        for (int i = 0; i <= amount; i++) {//��ö�ٽ��
            if ((long long)i + coins[j] <= (long long)amount) {
                    dp[i + coins[j]] += dp[i];
                }
            }
    }
    

    return dp[amount];
}