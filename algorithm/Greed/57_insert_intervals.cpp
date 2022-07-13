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
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>>::iterator iter = intervals.begin();
        while (iter != intervals.end()) {
            if ((*iter)[0] < newInterval[0] || ((*iter)[0] == newInterval[0] && (*iter)[1] < newInterval[1])) {
                iter++;
            } else {
                break;
            }
            
        }
        intervals.insert(iter, newInterval);

        return merge(intervals);
    }

    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> ans;
        for (int i = 0; i < intervals.size();) {
            int t = intervals[i][1];
            int j = i + 1;
            while (j < intervals.size() && intervals[j][0] <= t) {
                t = max(t, intervals[j][1]);//体现贪心：右端点越大越容易包含
                j++;   
            }
            ans.push_back({ intervals[i][0], t });
            i = j;
        }
        return ans;
    }
};

int main()
{
    return 0;
}
