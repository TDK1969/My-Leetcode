#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
#include <set>
using namespace std;

class Solution {
public:
    struct cmp {
        bool operator()(const vector<int>&a, const vector<int>&b) {
            return a[0] < b[0] || a[0] == b[0] && a[2] > b[2] || a[0] == b[0] && a[2] == b[2] && a[1] > b[1];
        }
    };

    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        multiset<vector<int>, cmp> h;
        vector<vector<int>> ans;
        int len = buildings.size();
        for (auto t : buildings) {
            h.insert(t);
        }
        vector<int> now_point = *(h.begin());
        h.erase(h.begin());

        while (!h.empty()) {
            vector<int> next_point = *(h.begin());
            h.erase(h.begin());
            //覆盖
            if (now_point[0] <= next_point[0] && now_point[2] >= next_point[2] && now_point[1] >= next_point[1]) {
                continue;
            }
            //相邻
            if (now_point[1] == next_point[0]) {
                vector<int> point {now_point[0], now_point[2]};
                ans.push_back(point);
                now_point = next_point;
            }
            //重合且同一高度
            else if (now_point[1] >= next_point[0] && now_point[2] == next_point[2]) {
                now_point[1] = max(now_point[1], next_point[1]);
            }
            //错开
            else if (now_point[1] < next_point[0]) {
                vector<int> point {now_point[0], now_point[2]};
                ans.push_back(point);
                vector<int> point2 {now_point[1], 0};
                ans.push_back(point2);
                now_point = next_point;
            }
            //重合，凸形
            else if (now_point[2] < next_point[2] && now_point[1] >= next_point[1]) {
                vector<int> point {now_point[0], now_point[2]};
                ans.push_back(point);
                vector<int> new_building {next_point[1], now_point[1], now_point[2]};
                h.insert(new_building);
                now_point = next_point;
            }
            //重合，高，右边突出
            else if (now_point[1] >= next_point[0] && now_point[2] < next_point[2]) {
                vector<int> point {now_point[0], now_point[2]};
                ans.push_back(point);
                now_point = next_point;
            }
            //重合，低，右边突出
            else if (now_point[1] >= next_point[0] && now_point[2] > next_point[2]) {
                vector<int> new_building {now_point[1], next_point[1], next_point[2]};
                h.insert(new_building);
            }
        }
        vector<int> point_final1 {now_point[0], now_point[2]};
        ans.push_back(point_final1);
        vector<int> point_final2 {now_point[1], 0};
        ans.push_back(point_final2);
        return ans;
    }
};

int main()
{
    Solution test;
    vector<vector<int>> buildings(5, vector<int>(3));
    buildings[0][0] = 2;
    buildings[0][1] = 9;
    buildings[0][2] = 10;
    buildings[1][0] = 3;
    buildings[1][1] = 7;
    buildings[1][2] = 15;
    buildings[2][0] = 5;
    buildings[2][1] = 12;
    buildings[2][2] = 12;
    buildings[3][0] = 15;
    buildings[3][1] = 20;
    buildings[3][2] = 10;
    buildings[4][0] = 19;
    buildings[4][1] = 24;
    buildings[4][2] = 8;
    test.getSkyline(buildings);
    return 0;
}
