from curses.ascii import SO
from typing import List
from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = defaultdict(int)
        lose = defaultdict(int)
        players = set()
        for match in matches:
            win[match[0]] += 1
            lose[match[1]] += 1
            players.add(match[0])
            players.add(match[1])
        
        ans = [[], []]

        for player in players:
            if lose[player] == 0 and win[player]:
                ans[0].append(player)
            elif lose[player] == 1:
                ans[1].append(player)
        
        ans[0].sort()
        ans[1].sort()

        return ans

test = Solution()
print(test.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))