#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s):
        longest_palindrome = ''
        dp = [[float("-inf")] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            longest_palindrome = s[i]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                #print("i: %d, j: %d" % (i,j))
                if s[i] == s[j]:  # if the chars mathces
                    if j - i == 1 or dp[i + 1][j - 1] is True:
                        dp[i][j] = True
                        if len(longest_palindrome) < (j+1-i):
                            longest_palindrome = s[i:j + 1]

        return longest_palindrome
