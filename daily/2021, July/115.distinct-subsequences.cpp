#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

//TODO:fix bugs
int dp[1000][1000];
class Solution {
public:
    int numDistinct(string s, string t) {
        for (int i = 0; i < s.length() + 1; i++) {
            dp[0][i] = 1;
        }

        for (int x = 1; x < t.length() + 1; x++) {
            for (int y = 1; y < s.length() + 1; y++) {
                dp[x][y] = dp[x][y - 1];
                if (t[x - 1] == s[y - 1]) {
                    dp[x][y] += dp[x - 1][y - 1];
                }
            }
        }

        return dp[t.length()][s.length()];
    }
};
