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
    int erase0verlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) {
            return 0;
        }
        sort(intervals.begin(), intervals.end());

        vector<int> prev = intervals[0];//prev记录上一个不重叠的区间
        int count = 0;

        for (int i = 1; i < intervals.size(); i++) {
            if (prev[1] > intervals[i][0]) {//如果发生重叠
                if (prev[1] >= intervals[i][1]) {//如果是覆盖重叠，取小区间
                    prev = intervals[i];
                }//如果是错位重叠，取前面的区间--》优先选择早结束的区间，会留下更多的选择空间，
                 //因为需要保留尽可能多的区间
                count++;
            } else {
                prev = intervals[i];
            }
        }

        return count;
    }
};  

int main()
{
    return 0;
}
