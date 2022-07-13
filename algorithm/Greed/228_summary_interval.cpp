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
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> ans;
        if (nums.size() == 0) {
            return {};
        }
        string temp;
        int left, right;
        bool isInterval = false;
        for (vector<int>::iterator iter = nums.begin(); iter < nums.end(); iter++) {
            if (!isInterval) {
                left = *iter;
                right = left;
                temp += to_string(left);
                isInterval = true;
            } else {
                if (*iter == right + 1) {
                    right++;
                } else {
                    if (left != right) {
                        temp += "->";
                        temp += to_string(right);
                    }
                    ans.push_back(temp);
                    temp.clear();
                    isInterval = false;
                    iter--;
                }
            }   
        }
        if (left != right) {
            temp += "->";
            temp += to_string(right);
        }
        ans.push_back(temp);
        temp.clear();

        return ans;
    }
};  

int main()
{
    Solution test;
    vector<int> arr(6);
    arr[0] = 0;
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 4;
    arr[4] = 5;
    arr[5] = 7;
    test.summaryRanges(arr);
    return 0;
}
