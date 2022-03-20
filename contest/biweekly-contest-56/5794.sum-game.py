class Solution:
    def sumGame(self, num: str) -> bool:
        term = num.count("?")
        if term & 1:
            return True
        mid = len(num) // 2
        left_term = num[:mid].count("?")
        right_term = num[mid:].count("?")

        left_sum = 0
        right_sum = 0
        for i in num[:mid]:
            if i != '?':
                left_sum += int(i)
        for i in num[mid:]:
            if i != '?':
                right_sum += int(i)
        Alice = True
        if left_sum >= right_sum:
            while left_term and right_term:
                if Alice:
                    left_term -= 1
                    left_sum += 9
                    Alice = not Alice
                else:
                    right_term -= 1
                    right_sum += 9
                    Alice = not Alice
        else:
            while left_term and right_term:
                if Alice:
                    right_term -= 1
                    right_sum += 9
                    Alice = not Alice
                else:
                    left_term -= 1
                    left_sum += 9
                    Alice = not Alice

        while left_term + right_term:
            if Alice:
                if left_sum >= right_sum:
                    if left_term:
                        left_term -= 1
                        left_sum += 9
                    elif right_term:
                        right_term -= 1
                        if left_sum - right_sum < 9:
                            right_sum += 9
                elif right_sum >= left_sum:
                    if right_term:
                        right_term -= 1
                        right_sum += 9
                    elif left_term:
                        left_term -= 1
                        if right_sum - left_sum < 9:
                            left_sum += 9
            elif not Alice:
                if left_sum >= right_sum:
                    if left_term:
                        left_term -= 1
                    elif right_term:
                        right_term -= 1
                        if left_sum - right_sum <= 9:
                            right_sum = left_sum
                        else:
                            right_sum += 9
                elif right_sum >= left_sum:
                    if right_term:
                        right_term -= 1
                    elif left_term:
                        left_term -= 1
                        if right_sum - left_sum <= 9:
                            left_sum = right_sum
                        else:
                            left_term += 9
            Alice = not Alice
            term -= 1

        if left_sum != right_sum:
            return True
        return False




test = Solution()
print(test.sumGame("?8???????0??8?4??1???2??4??1???1???8????2???4?49?34?"))