#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define min(x, y) x < y ? x : y

int coinChange(int* coins, int coinsSize, int amount)
{
    if (amount == 0) {
        return 0;
    }
    int *dp = (int *)malloc(sizeof(int) * (amount + 1));
    memset(dp, -1, sizeof(int) * (amount+ 1));

    for (int i = 0; i < coinsSize; i++) {
        if (coins[i] <= amount) {
            dp[coins[i]] = 1;
        }
    }

    if (dp[amount] == 1) {
        return 1;
    }

    for (int i = 1; i <= amount; i++) {
        if (dp[i] != -1) {
            for (int j = 0; j < coinsSize; j++) {
                if ((long long)i + coins[j] <= (long long)amount) {
                    if (dp[i + coins[j]] == -1) {
                        dp[i + coins[j]] = dp[i] + 1;
                    } else {
                        dp[i + coins[j]] = min(dp[i] + 1, dp[i + coins[j]]);
                    }
                }
            }
        }
    }

    return dp[amount];
}