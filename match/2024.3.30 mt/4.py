def solution(s: str) -> int:
    mod = (10 ** 9) + 7
    n = len(s)
    count = [0] * 26
    for c in s:
        count[ord(c) - ord("a")] += 1
    ans = 0

    h = [1] * 26
    nums = [i for i in range(26)]
    

    for l in range(2, n, 2):
        # 组成长度为l的平衡串子序列，每个字母应该有i个
        i = l // 2
        finish = []
        for index, value in enumerate(nums):
            # 更新h[j]为C(count[j], i)
            if count[value] >= i:
                h[value] = h[value] * (count[value] - i + 1) // i
            else:
                finish.append(index)
        for index in finish[::-1]:
            nums.pop(index)

        # 提前退出
        
        if len(nums) == 0 or len(nums) == 1:
            break
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                ans = (ans + h[nums[j]] * h[nums[k]]) % mod

    return ans


print(solution("ababa"))