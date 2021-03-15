#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int len = strs.size();
        vector<vector<vector<int>>> dp(len + 1, vector<vector<int>>(m + 1, vector<int>(n + 1, 0)));

        for (int i = 1; i <= len; i++) {
            vector<int> cnt = countZeroandOne(strs[i - 1]);

            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];

                    int zeros = cnt[0];
                    int ones = cnt[1];

                    if (j >= zeros && k >= ones) {
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1);
                    }
                }
            }
        }

        return dp[len][m][n];
    }
private:
    vector<int> countZeroandOne(string strs)
    {
        vector<int> cnt(2);
        for (int i = 0; i < strs.size(); i++) {
            cnt[strs[i] - '0']++;
        }
        return cnt;
    }
    
};

class Solution2 {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int S = strs.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int l = 0; l < S; ++l) {
            int zero = 0;
            int one = 0;
            for (int i = 0; i < strs[l].size(); ++i) {
                if (strs[l][i] == '0') ++zero;
                else ++one;
            }
            for (int i = m; i >= zero; --i) {
                for (int j = n; j >= one; --j) {
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zero][j - one]);
                }
            }
        }
        return dp[m][n];
    }
};