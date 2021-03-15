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
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        if (people.empty()) {
            return {};
        }
        vector<vector<int>> sorted_people;

        int count = people.size();
        while(count--) {
            int index = -1;
            int maxheight = -1;
            int lessk = 0x3f3f3f;
            vector<int> temp;
            for (int i = 0; i < people.size(); i++) {
                if (people[i][0] > maxheight || people[i][0] == maxheight && people[i][1] < lessk) {
                    maxheight = people[i][0];
                    lessk = people[i][1];
                    index = i;
                    temp = people[i];
                }
            }

            people[index][0] = -2;
            sorted_people.insert(sorted_people.begin() + temp[1], temp);
        }
        return sorted_people;
    }
};

int main()
{
    Solution test;
    vector<vector<int>> people;

    int n = 0;
    cin >> n;
    while(n--) {
        int height, k;
        vector<int> man;
        cin >> height >> k;
        man.push_back(height);
        man.push_back(k);
        people.push_back(man);
    }

    vector<vector<int>> newpeople = test.reconstructQueue(people);

    return 0;
}
