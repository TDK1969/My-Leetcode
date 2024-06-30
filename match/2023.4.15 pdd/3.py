from typing import List
import bisect

def solution(nums: List[int]) -> List[int]:
    s = sum(nums)
    presum = []
    for num in nums:
        if not presum:
            presum.append(num)
        else:
            presum.append(presum[-1] + num)
    
    presum_set = set(presum)

    def sliceSubSumK(k: int) -> int:
        # 将nums数组进行子数组和为k的完美拆分，如果能够完美拆分，返回厚度，否则返回0
        ans = 0
        p = -1
        for i in range(1, (s // k) + 1):
            q = bisect.bisect_left(presum, i * k)
            if presum[q] != i * k:
                return 0
            ans = max(ans, q - p)
            p = q
        return ans
        

    # 每个子数组的和>=m
    ans = [len(nums), s]
    m = max(nums)
    for i in presum_set:
        if i >= m and s % i == 0:
            res = sliceSubSumK(i)
            if res != 0 and res < ans[0]:
                ans[0], ans[1] = res, i
    return ans


print(solution([1,4,5]))