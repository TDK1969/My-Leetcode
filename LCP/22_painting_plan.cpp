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
    struct stack_elem{
        int paint_line;
        vector<vector<int>> board;
    };

    int paintingPlan(int n, int k) {
        if (k < n) {
            return 0;
        }

        vector<vector<int>> board(n, vector<int>(n));
        stack<stack_elem> mystack;

    }
};

int main()
{
    return 0;
}
