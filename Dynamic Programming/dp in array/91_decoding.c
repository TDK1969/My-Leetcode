#include <stdlib.h>
#include <string.h>
//他写测试用例一直可以的
#define max(x, y) (x > y) ? x : y

int numDecodings(char * s)
{   
    if (s[0] == '0') {
        return 0;
    }
    int len = strlen(s);
    if (len == 1) {
        if (s[0] == '0') {
            return 0;
        }
        return 1;
    }
    int *dp = (int *)malloc(sizeof(int) * len);
    memset(dp, 0, sizeof(int) * len);

    dp[0] = 1;
    if (10 * (s[0] - '0') + s[1] - '0' <= 26) {
        if (s[1] == '0') {
            if (s[0] == '0') {
                dp[1] = 0;
            } else {
                dp[1] = 1;
            }
        } else {
            dp[1] = 2;
        }
    } else {
        if (s[1] == '0') {
            dp[1] = 0;
            dp[0] = 0;
        } else {
            dp[1] = 1;
        }
    }

    for (int i = 2; i < len; i++) {
        int ans = 0;
        if (s[i] != '0') {
            ans = dp[i - 1];
        }
        if (10 * (s[i - 1] - '0') + s[i] - '0' <= 26) {
            if(s[i - 1] == '0' && s[i] == '0') {
                return 0;
            }
            if (s[i - 1] != '0') {
                ans += dp[i - 2];
            }
        }
        dp[i] = ans;
    }
    return dp[len - 1];
}