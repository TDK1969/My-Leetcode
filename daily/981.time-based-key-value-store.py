class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timemap = {}


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        value_time = self.timemap.setdefault(key, [])
        value_time.append((value, timestamp))




    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        value_time = self.timemap.get(key, None)
        if value_time:
            left = 0
            right = len(value_time) - 1
            if timestamp < value_time[left][1]:
                return ""
            while left <= right:
                mid = (left + right) // 2
                if timestamp > value_time[mid][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left >= len(value_time):
                return value_time[right][0]
            if right < 0:
                return value_time[left][0]
            if value_time[left][1] - timestamp < timestamp - value_time[right][1]:
                return value_time[left][0]
            else:
                return value_time[right][0]
        return ""





# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

test = TimeMap()
test.set("foo", "bar", 1)
print(test.get("foo", 1))
print(test.get("foo", 3))
test.set("foo", "bar2", 4)
print(test.get("foo", 4))
print(test.get("foo", 5))