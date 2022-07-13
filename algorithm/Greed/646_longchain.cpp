#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool cmp(vector<int> &x, vector<int> &y) {
        return x[1] < y[1];
    }

    int findLongestChain(vector<vector<int>>& pairs) {
        if (pairs.size() == 0) {
            return 0;
        }
        sort(pairs.begin(), pairs.end(), cmp);

        int count = 1;
        int right = pairs[0][1];

        for (int i = 0; i < pairs.size(); i++) {
            if (pairs[i][0] > right) {
                right = pairs[i][1];
                count++;
            }
        }

        return count;
    }
};

int main()
{
    return 0;
}
