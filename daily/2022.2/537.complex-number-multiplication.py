class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        s1, x1 = num1.split('+')
        s2, x2 = num2.split('+')
        s1 = int(s1)
        x1 = int(x1.split('i')[0])
        s2 = int(s2)
        x2 = int(x2.split('i')[0])

        s3 = s1 * s2 - x1 * x2
        x3 = s1 * x2 + s2 * x1
        ans = "{}+{}i".format(s3, x3)

        return ans
test = Solution()
print(test.complexNumberMultiply(num1 = "1+1i", num2 = "1+1i"))