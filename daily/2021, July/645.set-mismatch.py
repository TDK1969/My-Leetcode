class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        n = len(nums)
        correct = set(i for i in range(1, n + 1))
        lost = correct.difference(set(nums)).pop()
        repeat = - n * (n + 1) / 2 + sum(nums) + lost
        return [int(repeat), lost]
        """
        n = len(nums)
        numsum = sum(nums)
        repeat = numsum - sum(set(nums))
        lost = n * (n + 1) / 2 - numsum + repeat
        return [repeat, int(lost)]


