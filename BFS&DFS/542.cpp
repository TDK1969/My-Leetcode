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
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int a = matrix.size();
        int b = matrix[0].size();

        vector<vector<int>> dist(a, vector<int>(b, 0x3f3f3f));

        for (int i = 0; i < a; i++) {
            for (int j = 0; j < b; j++) {
                if (dist[i][j] == ) {

                }
            }
        }
    }

    int cal_dist(vector<vector<int>>& matrix, vector<vector<int>>& dist, int i, int j) {
        if (matrix[i][j] == 0) {
            dist[i][j] = 0;
            return 0;
        } else {

        }
    }
};

int main()
{
    return 0;
}

