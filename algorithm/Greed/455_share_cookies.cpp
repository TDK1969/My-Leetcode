#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    return 0;
}
//思路：贪心算法————尽量用尺寸小的饼干满足胃口小的孩子
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int cnt = 0;
        int i = 0;
        int j = 0;
        while(i < g.size()) {
            if (j == s.size()) {
                break;
            }

            if (s[j] >= g[i]) {
                i++;
                cnt++;
            }

            j++;
        }

        return cnt;
    }
};