class Solution:
    def largestInteger(self, num: int) -> int:
        num1 = str(num)        
        even = [num1[i] for i in range(len(num1)) if int(num1[i]) & 1 == 0]
        odd = [num1[i] for i in range(len(num1)) if int(num1[i]) & 1 == 1]
        even.sort(reverse=True)
        odd.sort(reverse=True)
        evenP = 0
        oddP = 0

        ans = ""
        for n in num1:
            if int(n) & 1 == 0:
                ans += even[evenP]
                evenP += 1
            else:
                ans += odd[oddP]
                oddP += 1
        
        return int(ans)
