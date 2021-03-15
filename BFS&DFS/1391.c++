#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    return 0;
}

class Solution {
public:
    bool hasValidPath(vector<vector<int>>& grid) {
        //vector<vector<int>> visited;
        vector<vector<int>> visited(grid.size(), vector<int>(grid[0].size(), 0));
        int x = 0;
        int y = 0;
        bool flag = 1;
        int a = grid.size();
        int b = grid[0].size();
        while (x != grid.size()-1 && y != grid[0].size()) {
            int val = grid[x][y];
            visited[x][y] = 1;
            if (val == 1) {
                if (y - 1 >= 0 && visited[x][y - 1] == 0) {
                    y = y - 1;
                } else if ( y + 1 <= b && visited[x][y + 1] == 0) {
                    y = y + 1;
                } else {
                    flag = 0;
                }
            }
            if (val == 2) {
                if (x - 1 >= 0 && visited[x - 1][y] == 0) {
                    x = x - 1;
                } else if ( x + 1 <= a && visited[x + 1][y] == 0) {
                    x = x + 1;
                } else {
                    flag = 0;
                }
            }
            if (val == 3) {
                if (y - 1 >= 0 && x - 1 >= 0 && visited[x - 1][y - 1] == 0) {
                    x = x - 1;
                    y = y - 1;
                } else if ( y + 1 <= b && x + 1 <= a && visited[x + 1][y + 1] == 0) {
                    x = x + 1;
                    y = y + 1;
                } else {
                    flag = 0;
                }
            }
            if (val == 4) {
                if (y - 1 >= 0 && x + 1 <= a && visited[x + 1][y - 1] == 0) {
                    x = x + 1;
                    y = y - 1;
                } else if (y + 1 <= b && x - 1 >= 0 && visited[x - 1][y + 1] == 0) {
                    x = x - 1;
                    y = y + 1;
                } else {
                    flag = 0;
                }
            }
            if (val == 5) {
                if (y - 1 >= 0 && x + 1 <= a && visited[x + 1][y - 1] == 0) {
                    x = x + 1;
                    y = y - 1;
                } else if (y + 1 <= b && x - 1 >= 0 && visited[x - 1][y + 1] == 0) {
                    x = x - 1;
                    y = y + 1;
                } else {
                    flag = 0;
                }
            }

        }
    }
};