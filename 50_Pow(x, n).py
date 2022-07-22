"""
Leetcode-https://leetcode.com/problems/powx-n/
TC- O(logN), SC- O(1)
Challenges-Coding binary solution
Lecture-https://www.youtube.com/watch?v=rWaQTam6Z7c
FAQ-


Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""


class Solution:
    """
    Ideation- Binary search, TC- O(logN), SC- O(1)

    The idea is to reduce repetitions. For example, to calculate 2^5, it can be done by calculating -
    2^2 * 2^2 * 2^1 * 2^1. 2^2 here is the repeated problem.

    Doing so, we can divide the sub problem in half each time and use it.
    """

    def myPow(self, x: float, n: int) -> float:
        # base
        if n == 0:
            return 1
        # floor division for negative doesn't give same result as positive in python
        result = self.myPow(x, int(n / 2))
        if n % 2 != 0:
            if n < 0:
                result = result * result * 1 / x
            else:
                result = result * result * x
        else:
            # if n is negative even, it would always call myPower(x, 1), because of n // 2, ex. 2//2=1.
            # Hence, we don't need to deal negative here.
            result = result * result

        return result

    """
    Ideation- Brute Force, TC- O(N), SC- O(1)

    Multiply x, n times.
    We will need to handle if n is negative. If so, our result will go in denominator by 1.
    """

    def myPow1(self, x: float, n: int) -> float:
        ans = 1
        for i in range(abs(n)):
            ans *= x

        # if n is negative, our result will be 1/ans
        if n < 0:
            return 1 / ans
        return ans / 1.0


x, n = 2.10000, 3
ans = Solution().myPow(x, n)
print(ans)
