class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        pre = [0]
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] == "1":
                pre.append(pre[-1] + 1)
            else:
                pre.append(pre[-1])
        for i in range(n):
            for j in range(i + 1, n + 1):
                # 表示子字符串s[i:j],验证是否是1显著
                cnt1 = pre[j] - pre[i]
                cnt0 = j - i - (pre[j] - pre[i])
                if cnt1 >= cnt0 * cnt0:
                    ans += 1
        return ans
