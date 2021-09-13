class Solution:
    def checkValidString(self, s: str) -> bool:
        star = []
        cnt = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                cnt.append(i)
            elif char == '*':
                star.append(i)
            elif char == ')':
                if cnt:
                    cnt.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while cnt and star:
            if cnt[-1] > star[-1]:
                return False
            cnt.pop()
            star.pop()
        return not cnt
test = Solution()
print(test.checkValidString("*("))