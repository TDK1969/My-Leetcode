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
// ˼·��Ҫʹÿ��ȡmin����ʧ��С����������Ҫ�㹻�ӽ�����������֮��ȡż������Ԫ�صĺͣ���Ϊ����ֵ
class Solution {
public:
    int arrayPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int sum = 0;
        for (int i = 0; i < nums.size(); i += 2) {
            sum += nums[i];
        }
        return sum;
    }
};