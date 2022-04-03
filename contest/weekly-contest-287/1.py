class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur = current.split(':')
        cor = correct.split(':')
        curH, curM = int(cur[0]), int(cur[1])
        corH, corM = int(cor[0]), int(cor[1])
        ans = 0
        if curM > corM:
            corM += 60
            corH -= 1
        ans += corH - curH
        ans += (corM - curM) // 15
        temp = (corM - curM) % 15
        ans += temp // 5
        temp = temp % 5
        ans += temp

        return ans