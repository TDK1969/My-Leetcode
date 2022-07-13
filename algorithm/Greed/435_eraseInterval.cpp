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
    int erase0verlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) {
            return 0;
        }
        sort(intervals.begin(), intervals.end());

        vector<int> prev = intervals[0];//prev��¼��һ�����ص�������
        int count = 0;

        for (int i = 1; i < intervals.size(); i++) {
            if (prev[1] > intervals[i][0]) {//��������ص�
                if (prev[1] >= intervals[i][1]) {//����Ǹ����ص���ȡС����
                    prev = intervals[i];
                }//����Ǵ�λ�ص���ȡǰ�������--������ѡ������������䣬�����¸����ѡ��ռ䣬
                 //��Ϊ��Ҫ���������ܶ������
                count++;
            } else {
                prev = intervals[i];
            }
        }

        return count;
    }
};  

int main()
{
    return 0;
}
