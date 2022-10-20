from typing import *
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        ans = set()
        cnt = []
        def dfs(k: int):
            if k == 1:
                ans.add(frozenset(cnt))
                return
            for i in range(2, k):
                if i ** 2 > k:
                    break
                if k % i == 0:
                    cnt.append(i)
                    cnt.append(k // i)
                    ans.add(frozenset(cnt))
                    cnt.pop()
                    dfs(k // i)
                    cnt.pop()
        dfs(n)
        ans = [list(i) for i in ans]
        return ans
t = Solution()
print(t.getFactors(32))


