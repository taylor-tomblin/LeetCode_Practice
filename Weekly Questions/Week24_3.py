"""
1259. Handshakes That Don't Cross
(Hard)

You are given an even number of people numPeople that stand around a circle and each person shakes hands with someone else so that there are numPeople / 2 handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since the answer could be very large, return it modulo 109 + 7.

Example 1:
Input: numPeople = 4
Output: 2
Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is [(2,3),(4,1)].

Example 2:
Input: numPeople = 6
Output: 5
Input: numPeople = 6
Output: 5
 

Constraints:
    - 2 <= numPeople <= 1000
    - numPeople is even.
"""

class Solution(object):
    def numberOfWays(self, numPeople):
        """
        :type numPeople: int
        :rtype: int
        """
        mod = 10**9 + 7
        dp = [0] * (numPeople + 1)
        dp[0] = 1

        for i in range(2, numPeople + 1, 2):
            for j in range(0, i, 2):
                dp[i] = (dp[i] + dp[j] * dp[i - 2 - j]) % mod

        return dp[numPeople]