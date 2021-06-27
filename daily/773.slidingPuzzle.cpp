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
    int slidingPuzzle(vector<vector<int>>& board) {
        vector<int> step(44800, -1);
        vector<vector<vector<int>>> puzzle;
        step[getvalue(board)] = 0;
        puzzle.push_back(board);

        while (!puzzle.empty()) {
            vector<vector<int>> temp = puzzle[0];
            puzzle.erase(puzzle.begin());
            int tempvalue = getvalue(temp);
            if (tempvalue == 11190) {
                return step[11190];
            }

            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 3; j++) {
                    if (temp[i][j] == 0) {
                        if (i == 0) {
                            vector<vector<int>> nextboard = temp;
                            swap(nextboard[i][j], nextboard[i + 1][j]);
                            int nextstep = getvalue(nextboard);
                            if (step[nextstep] == -1) {
                                step[getvalue(nextboard)] = step[tempvalue] + 1;
                                if (nextstep == 11190) {
                                    return step[11190];
                                }
                                puzzle.push_back(nextboard);
                            }
                        } else {
                            vector<vector<int>> nextboard = temp;
                            swap(nextboard[i][j], nextboard[i - 1][j]);
                            int nextstep = getvalue(nextboard);
                            if (step[nextstep] == -1) {
                                step[getvalue(nextboard)] = step[tempvalue] + 1;
                                if (nextstep == 11190) {
                                    return step[11190];
                                }
                                puzzle.push_back(nextboard);
                            }
                        }

                        for (int x = -1; x < 2; x++) {
                            if (j + x < 0 || j + x > 2 || x == 0) {
                                continue;
                            }
                            vector<vector<int>> nextboard = temp;
                            swap(nextboard[i][j], nextboard[i][j + x]);
                            int nextstep = getvalue(nextboard);
                            
                            if (step[nextstep] == -1) {
                                step[getvalue(nextboard)] = step[tempvalue] + 1;
                                if (nextstep == 11190) {
                                    return step[11190];
                                }
                                puzzle.push_back(nextboard);
                            }
                        }
                    }

                }
            }
        }

        return -1;


    }
    int getvalue(vector<vector<int>>& board) {
        return board[0][0]*6*6*6*6*6 + board[0][1]*6*6*6*6 + board[0][2]*6*6*6 + \
                board[1][0]*6*6 + board[1][1]*6 + board[1][2];
    }
        
};

int main()
{
    Solution test;
    vector<vector<int>> board;
    vector<int> line1 = {1, 2, 3};
    vector<int> line2 = {4, 0, 5};
    board.push_back(line1);
    board.push_back(line2);
    printf("%d\n", test.slidingPuzzle(board));
    return 0;
}
