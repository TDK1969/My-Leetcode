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
    string convertToTitle(int columnNumber) {
        string title;

        while (columnNumber != 0) {
            int temp = (columnNumber % 26 == 0) ? 26 : columnNumber % 26;
            string bit(1, 'A' + temp - 1);
            title = bit + title;
            columnNumber = (temp == 26) ? columnNumber / 26 - 1 : columnNumber / 26;
            
        }
        return title;
    }
};

int main()
{
    Solution test;
    printf("%d\n", test.convertToTitle(52));
    return 0;
}
