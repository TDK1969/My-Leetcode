# 贪心算法一题多解

## 121. 炒股的最佳时机
1. 贪心算法
    开始亏钱就重新买，赚钱就更新max，返回max
    
    ```cpp
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
    ```
    
    
    
2. 维护单调栈

```cpp
int maxProfit(vector<int>& prices) {
        int ans = 0;
        vector<int> St;
        prices.emplace_back(-1);
        for (int i = 0; i < prices.size(); ++ i){
            while (!St.empty() && St.back() > prices[i]){
                ans = max(ans, St.back() - St.front()); 
                St.pop_back();
            }
            St.emplace_back(prices[i]);
        }

        return ans;
    }
```

?	