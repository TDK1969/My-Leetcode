from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        bobArrows = numArrows
        ans = [0] * 12

        for i in range(11, -1, -1):
            if bobArrows == 0:
                break
            if aliceArrows[i] * 2 > bobArrows:
                continue
            else:
                ans[i] = aliceArrows[i] + 1
                bobArrows -= aliceArrows[i] + 1
        return ans

test = Solution()
print(test.maximumBobPoints(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]))