class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        
        if len(n) == 1:
            return str(num - 1)
        elif num == 10 ** (len(n) - 1):
            return str(num - 1)
        nine = 10 ** (len(n) - 1) - 1
        minAbs = abs(num - nine)
        ans = str(nine)
        nxt = 10 ** (len(n)) + 1
        if abs(nxt - num) < minAbs:
            minAbs = abs(nxt - n)
            ans = str(nxt)
        
        for i in range(-1, 2):
            if len(n) & 1 == 1:
                half = str(int(n[:len(n) // 2]) + i)
                pNum = half + n[len(n) // 2] + half[::-1]
            else:
                half = str(int(n[:len(n) // 2]) + i)
                pNum = half + half[::-1]
            if pNum == n:
                continue
            elif abs(int(pNum) - num) < minAbs:
                    ans = pNum
                    minAbs = abs(int(pNum) - num)
        return ans

test = Solution()
print(test.nearestPalindromic( n = "11"))