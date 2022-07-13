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
        vector<int> stock;
        int profitsum = 0;
        prices.push_back(-1);
        for (int i = 0; i < prices.size(); i++) {
            if (!stock.empty() && stock.back() > prices[i]) {
                profitsum += stock.back() - stock.front();
                stock.clear();
            }
            stock.push_back(prices[i]);
        }
        return profitsum;
    }
};