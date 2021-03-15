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
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());//体现贪心：左端点越小越容易被包含
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
    Solution test;
    vector<vector<int>> intervals;
    vector<int> arr1(2);
    arr1[0] = 1;
    arr1[1] = 4;
    intervals.push_back(arr1);
    arr1[0] = 4;
    arr1[1] = 5;
    intervals.push_back(arr1);
    
    test.merge(intervals);
    return 0;
}
