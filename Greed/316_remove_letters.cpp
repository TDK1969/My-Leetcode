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
    bool judge(int index, stack<char> letterStack, vector<int> letters, vector<int> letterExist) {
        if (letterStack.empty() || letterExist[index]) {
            return false;
        }
        if (letterExist[index] == 0) {
            if (letters[letterStack.top() - 'a'] > 1 && letterStack.top() > )
        }
    }
    string removeDuplicateLetters(string s) {
        if (s.empty()) {
            return s;
        }
        vector<int> letters(26);
        for (int i = 0; i < s.size(); i++) {
            letters[s[i] - 'a']++;
        }

        stack<char> letterStack;
        vector<int> letterExist(26);
        for (int i = 0; i < s.size(); i++) {
            if (letterStack.empty()) {
                letterStack.push(s[i]);
            } else {
                while (!letterStack.empty() && letters[letterStack.top() - 'a'] > 1 && letterStack.top() > s[i]) {
                    letterStack.pop();
                }
                letterStack.push(s[i]);
                letters[s[i] - 'a']--;
                letterExist[s[i] - 'a']++;
            }
        }

        string newstring;
        while (!letterStack.empty()) {
            newstring = letterStack.top() + newstring;
            letterStack.pop();
        }
        return newstring;
    }
};

int main()
{
    return 0;
}
