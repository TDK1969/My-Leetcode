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
    for (int i = 1; i < len; i++) {
        if (s[i] == '0' && s[i - 1] != '1' && s[i - 1] != '2' && s[i - 1] != '*') {
            return 0;
        }
    }

    int *dp = (int *)malloc(sizeof(int) * len);
    memset(dp, 0, sizeof(int) * len);

    if (s[0] != '*') {
        dp[0] = 1;
    } else {
        dp[0] = 9;
    }
    
    if (s[0] == '*') {
        
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