#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <map>  
#include <algorithm>
using namespace std;

//贪心思路：先排序，每次贪心地先爆排序前的，然后贪心地尽量靠右侧爆
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) {
            return 0;
        }
        sort(points.begin(), points.end());
        int left, right;
        int count = 0;

        for (int i = 0; i < points.size(); i++) {
            left = points[i][0];
            right = points[i][1];

            while (i + 1 < points.size()) {
                if (points[i + 1][0] <= right) {
                    left = points[i + 1][0];
                    right = min(right, points[i + 1][1]);
                    i++;
                } else {
                    break;
                }
            }
            count++;
        }
        return count;
    }
};

int main()
{
    return 0;
}
