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
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26);

        for (int i = 0; i < tasks.size(); i++) {
            count[tasks[i]-'A']++;
        }//统计词频
        sort(count.begin(), count.end());//词频排序，升序排序，count[25]是频率最高的
        int maxCount = 0;
        //统计有多少个频率最高的字母
        for (int i = 25; i >= 0; i--) {
            if(count[i] != count[25]){
                break;
            }
            maxCount++;
        }
        int time = (count[25] - 1) * (n + 1) + maxCount; 
        //公式算出的值可能会比数组的长度小，取两者中最大的那个
        
        return time > tasks.size() ? time : tasks.size();
    }
};

class Solution2 {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> count(26);
        for (char ch : tasks) {
            count[ch - 'A']++;
        }

        sort(count.begin(), count.end());
        int time = 0;
        while (count[25] > 0) {//我们每一轮选择不超过 n + 1 个任务执行，直到所有的任务被执行
            int i = 0;
            while (i <= n) {
                if (count[25] == 0) {
                    break;
                }
                if (i < 26 && count[25 - i] > 0) {//不满足则是待机
                    count[25 - i]--;
                } 
                time++;
                i++;
            }
            sort(count.begin(), count.end());//排序——贪心地将出现次数较多的任务安排在前面
        }
        return time;
    }
};



int main()
{
    Solution test;
    vector<char> tasks(3, 'A');
    tasks.push_back('B');
    tasks.push_back('B');
    tasks.push_back('B');

    test.leastInterval(tasks, 2);
    return 0;
}
