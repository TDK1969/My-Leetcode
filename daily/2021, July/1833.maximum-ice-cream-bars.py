class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        sorted_costs = sorted(costs)
        left = coins
        count = 0
        for cost in sorted_costs:
            if cost <= left:
                left -= cost
                count += 1
            else:
                break
        return count
