# ̰���㷨һ����

## 121. ���ɵ����ʱ��
1. ̰���㷨
    ��ʼ��Ǯ��������׬Ǯ�͸���max������max
    
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
    
    
    
2. ά������ջ

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