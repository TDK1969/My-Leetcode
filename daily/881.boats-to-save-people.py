from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        ans = 0
        tight = 0
        heavy = n - 1
        while tight <= heavy:
            if people[heavy] + people[tight] <= limit:
                tight += 1
            heavy -= 1
            ans += 1
        return ans
