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
        }//ͳ�ƴ�Ƶ
        sort(count.begin(), count.end());//��Ƶ������������count[25]��Ƶ����ߵ�
        int maxCount = 0;
        //ͳ���ж��ٸ�Ƶ����ߵ���ĸ
        for (int i = 25; i >= 0; i--) {
            if(count[i] != count[25]){
                break;
            }
            maxCount++;
        }
        int time = (count[25] - 1) * (n + 1) + maxCount; 
        //��ʽ�����ֵ���ܻ������ĳ���С��ȡ�����������Ǹ�
        
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
        while (count[25] > 0) {//����ÿһ��ѡ�񲻳��� n + 1 ������ִ�У�ֱ�����е�����ִ��
            int i = 0;
            while (i <= n) {
                if (count[25] == 0) {
                    break;
                }
                if (i < 26 && count[25 - i] > 0) {//���������Ǵ���
                    count[25 - i]--;
                } 
                time++;
                i++;
            }
            sort(count.begin(), count.end());//���򡪡�̰�ĵؽ����ִ����϶����������ǰ��
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
