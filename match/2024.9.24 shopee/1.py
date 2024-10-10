class Solution:
    def maxLength(self, arr) :
        # write code here
        s = set()
        left = right = 0
        ans = -1
        n = len(arr)
        while right < n:
            if arr[right] in s:
                s.pop(arr[left])
                left += 1
            s.add(arr[right])
            right += 1
            ans = max(ans, right - left)
        return ans

print(Solution().maxLength([2,3,4,5]))