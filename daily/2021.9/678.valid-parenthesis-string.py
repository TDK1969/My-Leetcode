class Solution:
    def checkValidString(self, s: str) -> bool:
        star = [] # 记录*的下标的栈
        cnt = []  # 记录(的下标的栈

        for i in range(len(s)):
            char = s[i]
            if char == "(":
                cnt.append(i)
            elif char == '*':
                star.append(i)
            elif char == ')':
                # 优先匹配cnt栈中的(,因为*即使多了也可以当成空字符串
                if cnt:
                    cnt.pop()
                elif star:
                    star.pop()
                else:
                    # (和*都无法匹配,错误
                    return False
        # 开始处理多余的(和*
        while cnt and star:
            # (和*能够匹配的条件:*在(后面，才能变成)进行匹配
            if cnt[-1] > star[-1]:
                return False
            cnt.pop()
            star.pop(),
        # 如果cnt不为空，则还有多余的(,返回错误
        return not cnt
test = Solution()
print(test.checkValidString("*("))