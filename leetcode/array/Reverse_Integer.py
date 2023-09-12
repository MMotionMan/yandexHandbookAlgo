import math


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31-1
        MIN_INT = -2 ** 31

        answer = 0

        while x != 0:
            if answer > MAX_INT or answer < MIN_INT:
                return 0
            digit = x % 10 if x > 0 else x % -10
            answer = answer * 10 + digit
            x = math.trunc(x / 10)
        return answer


s = int(input())
sol = Solution()
print(sol.reverse(s))
