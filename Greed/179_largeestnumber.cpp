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
    static bool cmp(int &a, int &b) {
        return to_string(a) + to_string(b) > to_string(b) + to_string(a);
    }

    string largestNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end(), cmp);
        if (nums[0] == 0) {
            return "0";
        }
        string ans;
        for (int op : nums) {
            ans += to_string(op);
        }
        
        return ans;
    }
};

int main()
{
    return 0;
}

