class Solution:
    def reverses(self, original_str: str) :
        # write code here
        ans = list(original_str)
        n = len(original_str)
        cnt_lower = ""
        i = 0
        while i < n:
            if original_str[i] != " ":
                j = i
                cnt_lower = []
                while j < n and original_str[j] != " ":
                    if 97 <= ord(original_str[j]) <= 122:
                        cnt_lower.append(j)
                    j += 1
                p, q = 0, len(cnt_lower) - 1
                while p <= q:
                    ans[cnt_lower[p]], ans[cnt_lower[q]] = ans[cnt_lower[q]], ans[cnt_lower[p]]
                    p += 1
                    q -= 1
                i = j
            else:
                i += 1

        return "".join(ans)

    def reverses2(self, original_str: str) :
        # write code here
        ans = ""
        n = len(original_str)
        others = []
        for i in range(n):
            if not 97 <= ord(original_str[i]) <= 122:
                # 小写字母
                others.append(i)
        
        for k in range(len(others)):
            ans += original_str[others[k]]
            if k < len(others) - 1 and others[k + 1] - others[k] > 1:
                # 处理original_str[others[k] + 1:others[k + 1]]中的小写字母串
                for j in range(others[k + 1] - 1, others[k], -1):
                    ans += original_str[j]

        return ans

print(Solution().reverses("abCd"))
