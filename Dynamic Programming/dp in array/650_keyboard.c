#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int minSteps(int n)
{
    int *dp = (int *)malloc(sizeof(int) * (n + 1));
    memset(dp, 0, sizeof(int) * (n + 1));

    dp[1] = 0;
    for (int i = 2; i <= n; i++) {
        int temp = 1;
        for (int j = 2; j < i; j++) {
            if (i % j == 0) {
                temp = j;
            }
        }
        dp[i] = dp[temp] + i / temp;
    }
    return dp[n - 1];
}
//一次计算中不用重复，可以直接递归
int minSteps2(int n) {
    if (n == 1) {
        return 0;
    }
    for (int i = n / 2; i > 1; i--) {
        if (n % i == 0) {
            return minSteps(i) + n / i;
        }
    }
    return n;
}