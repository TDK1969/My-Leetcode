#include <cstdio>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    return 0;
}
//TODO:fix bugs
class Solution {
public:
    struct stack_elem {
        int s_count;
        int t_count;
    };

    int a(string s, string t, int s_count, int t_count, vector<int> &num) {
        if (t_count == t.length() - 1) {
            num[s_count] = 1;
            return 1;
        } else {
            for (int j = s_count + 1; j < s.length(); j++) {
                if (s[j] == t[t_count + 1]) {
                    if (num[j] != 0) {
                        num[s_count] += num[j];
                    } else {
                        num[s_count] += a(s, t, j, t_count + 1, num);
                    }
                }
            }
            return num[s_count];
        }
    }
    int numDistinct(string s, string t) {
        vector<int> num;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == t[0]) {
                num.insert(num.begin(), i);
            }
        }
        int ans = 0;
        for (int i = 0; i < num.size(); i++) {
            ans += a(s, t, i, 0, num);
        }
        return ans;
    }
    int numDistinct1(string s, string t) {
        vector<stack_elem> mystack;
        vector<int> num(s.length(), 0);
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == t[0]) {
                stack_elem temp;
                temp.s_count = i;
                temp.t_count = 0;
                mystack.push_back(temp);
            }
        }

        while (!mystack.empty()) {
            stack_elem rear = mystack.back();
            mystack.pop_back();
            if (rear.t_count == t.length() - 1) {
                count++;
                num[rear.s_count] = 1;
            } else {
                for (int j = rear.s_count + 1; j < s.length(); j++) {
                    if (s[j] == t[rear.t_count + 1]) {
                        stack_elem temp;
                        temp.s_count = j;
                        temp.t_count = rear.t_count + 1;
                        mystack.push_back(temp);
                    }
                }
            }
        }
        return count;
    }
};