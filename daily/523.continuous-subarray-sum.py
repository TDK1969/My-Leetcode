class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        yushu = set()
        sum = 0
        for num in nums:
            sum += num
            if (sum % k) in yushu:
                return True
            yushu.add((sum - num) % k)
        return False