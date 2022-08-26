from typing import *

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = [0]
        for i in blocks:
            white.append(white[-1] + (1 if i == "W" else 0))
        ans = len(blocks)

        for i in range(len(blocks) - k + 1):
            ans = min(ans, white[i + k] - white[i])
        return ans