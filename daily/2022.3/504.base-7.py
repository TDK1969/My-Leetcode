class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        flag = True if num >= 0 else False
        num = abs(num)

        ans = ''
        while num:
            ans = str(num % 7) + ans
            num = num // 7
        return ans if flag else '-' + ans