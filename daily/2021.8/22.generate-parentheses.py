from typing import List
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        queue = deque()
        queue.append(("", 0, 0))
        ans = []

        while queue:
            s, uc, cnt = queue.popleft()
            if len(s) == 2 * n:
                ans.append(s)
                continue
            if cnt < n:
                queue.append((s + '(', uc + 1, cnt + 1))
            if uc > 0:
                queue.append((s + ')', uc - 1, cnt))

        return ans

test = Solution()
print(test.generateParenthesis(4))
