
s = input()

ans = ""
j = 0
i = 0
while i < len(s):
    # 如果当前字符是小写字母
    if 'a' <= s[i] <= 'z':
        j = i + 1
        # 找到连续的小写字母
        while j < len(s) and 'a' <= s[j] <= 'z':
            j += 1
        # 将这些小写字母反转后添加到结果中
        ans += s[i:j][::-1]
        i = j
    else:
        # 如果当前字符不是小写字母，直接添加到结果中
        ans += s[i]
        i += 1

print(ans)