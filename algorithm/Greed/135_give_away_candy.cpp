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
//˼·����Ȼ���Ҷ�Ҫ���㣬�ǲ������Ҹ�����һ��
//����̰�ģ��ڱ��������У�ÿһ���������ٸ��ǣ�����ӵ�ʱ���һ����������̰��˼��
//��ÿ��ѡ��ʱ���Ծֲ�����Ϊ���򣬶������Ǵ˴β������Ժ������Ӱ�졣
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