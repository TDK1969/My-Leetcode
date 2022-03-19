class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        if numRows >= n:
            return s
        
        ans = []
        for i in range(numRows):
            j = i
            flag = True
            while j < n:
                ans.append(s[j])
                if i == 0 or i == numRows - 1:
                    j += 2 * (numRows - 1)
                elif flag:
                    j += 2 * (numRows - i - 1)
                else:
                    j += 2 * i
                flag = not flag
        return "".join(ans)

test = Solution()
print(test.convert(s = "PAYPALISHIRING", numRows = 3))
