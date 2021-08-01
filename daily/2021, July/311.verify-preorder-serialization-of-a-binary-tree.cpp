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
    bool isValidSerialization(string preorder) {
        vector<char> a;
        for (int i = 0; i < preorder.length(); i++) {
            a.push_back(preorder[i]);
            if (a.size() > 1 && a[0] == '#') {
                return false;
            }
            if (a.size() >= 3) {
                if (a[a.size() - 1] == '#' && a[a.size() - 2] == '#') {
                    a.pop_back();
                    a.pop_back();
                    a.pop_back();
                    a.push_back('#');
                }
            }
        }
        if (a.size() != 1) {
            return false;
        }
        return true;
    }
};

int main()
{
    string test = "934##1##2#6##";
    Solution a;
    a.isValidSerialization(test);
}
