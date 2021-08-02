from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        fight = [] 
        for i in range(len(mat)):
            fight.append((sum(mat[i]), i))
        fight.sort()
        ans = [x[1] for x in fight[:k]]
        return ans

test = Solution()
print(test.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3))
