#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

//˼·�����Ƶ���ջ�������Ƚ�������
class Solution {
public:
    int longestPalindrome(string s) {
        sort(s.begin(), s.end());
        s.push_back('*');
        int single = 0;
        int len = 0;
        vector<char> count;

        for (char letter : s) {
            if (!count.empty() && count[0] != letter) {
                if (!single && count.size() & 1) {
                    single = 1;
                    len += count.size();
                } else {
                    len += (count.size() / 2) * 2;
                }
                count.clear();
            }
            count.push_back(letter);
        }
        return len;
    }
};

//˼·��ͳ�������������ַ��飬��ϣ��
class Solution2 {
public:
    int longestPalindrome(string s) {
        map<char, int> count;
        int odd = 0;
        int len = s.size();

        for (char ch : s) {
            count[ch]++;
        }

        for (auto p : count) {
            odd += (p.second % 2);
        }

        return odd == 0 ? len : (len - odd + 1);
    }
};

int main()
{
    string s("abccccdd");
    Solution test;
    int ans = test.longestPalindrome(s);
    return 0;
}