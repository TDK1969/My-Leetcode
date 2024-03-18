from typing import List

def func(nums: List[int]) -> bool:
    # 输入为题目给定的数组
    max_num = max(nums)
    n = len(nums)
    nums_1 = [((max_num - i) % 2) + 1 for i in nums]
    dp = [0 for _ in range(n + 2)]
    # dp[i]表示前i个数四种状态:
        # 0 - 0b00 - 不能变成相同  
        # 1 - 0b01 - 只能变成0   
        # 2 - 0b10 - 只能变成1     
        # 3 - 0b11 - 可以变为0或1
    # 这样位运算处理的好处是 3 = 1 | 2，可以简化代码

    # 初始化dp数组,前两个是填充边界,设为3,从第三个开始
    dp[0] = dp[1] = 3
    dp[2] = nums_1[0]

    for i in range(1, n):
        # i是nums_1的下标, j是dp的下标,存在一个+2的偏移,仅在代码中使用,不影响逻辑
        j = i + 2
        # dp[j]的取值需要考虑三方面:
        # 下面为了理解方便,将<前j个数>表述为<前i个数>,仅作为理解
        # 若第i个数为k,且前i - 1个数可变成k,则前i个数可变成k
        if nums_1[i] & dp[j - 1]:
            dp[j] |= nums_1[i]

        # 若前i - 1个数可变为~k,且第i个数与第i-1个数相同为k,则可将第i个数与第i-1个数一起+1,变为~k,因此前i个数可变为~k
        if dp[j - 2] & (3 ^ nums_1[i]) and nums_1[i] == nums_1[i - 1]:
            dp[j] |= (3 ^ nums_1[i])

        # 若当前处理的数字数量为偶数,且前i个数可变成相同,则设为3,因为长度是偶数,可以两两配对+1
        if i % 2 == 1 and dp[j]:
            dp[j] = 3

    return dp[-1] != 0

print(func([0, 0, 1, 0, 0]))
            