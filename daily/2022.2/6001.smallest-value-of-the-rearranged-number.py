class Solution:
    def smallestNumber(self, num: int) -> int:
        flag = num >= 0
        if not flag:
            num = -num
        strNum = list(str(num))
        zeros = strNum.count('0')

        if zeros == len(strNum):
            return 0

        for _ in range(zeros):
            strNum.remove('0')

        if flag:
            strNum.sort()
            ans = ''
            ans += strNum[0]
            for _ in range(zeros):
                ans += '0'
            if len(strNum) > 1:
                ans += ''.join(strNum[1:])
        else:
            strNum.sort(reverse=True)
            ans = ''
            ans += ''.join(strNum[0:])
            for _ in range(zeros):
                ans += '0'
        temp = int(ans)
        if not flag:
            temp = -temp

        return temp

test = Solution()
print(test.smallestNumber(1))