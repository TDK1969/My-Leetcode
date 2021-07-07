import collections
class Solution1(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: list[int]
        :rtype: int
        """
        #deliciousness.sort()
        count = 0
        dishes = set(deliciousness)
        mod = 10 ** 9 + 7
        dish_count = collections.defaultdict(int)
        for dish in deliciousness:
            dish_count[dish] += 1

        for dish in dishes:
            for i in range(0, 22):
                rest = 2 ** i - dish
                if 2**i >= dish and rest in dishes:
                    if dish == rest:
                        count += (dish_count[dish] - 1) * dish_count[dish]
                        #print(dish, rest, (deliciousness.count(dish) - 1) * deliciousness.count(dish))
                    else:
                        count += dish_count[dish] * dish_count[rest]
                        #print(dish, rest, deliciousness.count(dish) * deliciousness.count(rest))

        count //= 2
        return count % mod

class Solution:
    mod = 10 ** 9 + 7
    maximum = 1 << 22
    def countPairs(self, deliciousness) -> int:
        hashmap = collections.Counter(deliciousness)
        ans = 0
        for x in hashmap:
            i = 1
            while i < self.maximum:
                t = i - x
                if t in hashmap:
                    if t == x:
                        ans += (hashmap[x] - 1) * hashmap[x]
                        print(t, x, (hashmap[x] - 1) * hashmap[x])
                    else:
                        ans += hashmap[x] * hashmap[t]
                        print(t, x, hashmap[x] * hashmap[t])
                i <<= 1
        ans >>= 1
        return ans % self.mod
