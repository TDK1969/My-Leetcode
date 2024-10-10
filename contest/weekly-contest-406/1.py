from collections import Counter, defaultdict
from typing import List
class Solution:
    def getSmallestString(self, s: str) -> str:
        ss = list(s)
        n = len(s)
        for i in range(n - 1):
            if ord(ss[i]) & 1 == ord(ss[i + 1]) & 1 and ord(ss[i]) > ord(ss[i + 1]):
                ss[i], ss[i + 1] = ss[i + 1], ss[i]
                break
        return "".join(ss)


            
        
