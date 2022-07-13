#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
    return 0;
}
//思路：既然左右都要满足，那不妨左右各遍历一趟
//体现贪心：在遍历过程中，每一步都尽量少给糖，必须加的时候加一个，体现了贪心思想
//在每次选择时，以局部最优为导向，而不考虑此次操作对以后操作的影响。
class Solution {
public:
    int candy(vector<int>& ratings) {
        int sum = 0;
        int len = ratings.size();
        vector<int> candy(len, 1);
        for (int i = 1; i < len; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candy[i] = candy[i - 1] + 1;
            }
        }
        for (int i = len - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1] && candy[i] <= candy[i + 1]) {
                candy[i] = candy[i + 1] + 1;
            }
        }

        for (int it : candy) {
            sum += it;
        }
        return sum;
    }
};