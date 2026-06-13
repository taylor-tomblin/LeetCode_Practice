"""
4. Longest Palindromic Substring
(Medium)

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
    - 1 <= s.length <= 1000
    - s consist of only digits and English letters.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start = 0
        max_length = 1

        for i in range(len(s)):
            # Odd length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

            # Even length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start = left
                    max_length = right - left + 1
                left -= 1
                right += 1

        return s[start:start + max_length]