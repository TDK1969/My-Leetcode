from collections import deque
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        od = ""
        while od != dominoes:
            od = dominoes
            dominoes = dominoes.replace("R.L", "A")
            dominoes = dominoes.replace(".L", "LL")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace("A", "R.L")
        return dominoes

test = Solution()
print(test.pushDominoes(".L.R...LR..L.."))