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
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxearn = 0;
        int buy = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < prices[buy]) {
                buy = i;
            } else {
                maxearn = max(maxearn, prices[i] - prices[buy]);
            }
        }
        return maxearn;
    }
};

class Solution2 {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        vector<int> St;
        prices.emplace_back(-1); // из╠Ь
        for (int i = 0; i < prices.size(); ++ i){
            while (!St.empty() && St.back() > prices[i]){ 
                ans = std::max(ans, St.back() - St.front()); 
                St.pop_back();
            }
            St.emplace_back(prices[i]);
        }

        return ans;
    }
};
